<?php
/**
 * Imports the Get Fit Elementor build into WordPress.
 *
 *   wp eval-file tools/import-to-wordpress.php [<git-ref>]
 *
 * Reads elementor/*.json and the theme assets from this repository (raw GitHub
 * URLs, so it also works on hosts where only WP-CLI is available) and:
 *  - merges kit.json into the active Elementor kit (global colours, fonts, layout),
 *  - creates/updates the UAE header and footer templates (display: entire site),
 *  - creates/updates the "Home" page and makes it the static front page,
 *  - stores the design CSS/JS in the getfit_css / getfit_js options and writes
 *    them to the child theme's assets/ folder,
 *  - clears Elementor's generated CSS so everything is rebuilt.
 *
 * Safe to run repeatedly: posts are matched by slug and updated in place.
 */

defined( 'ABSPATH' ) || exit;

$getfit_ref  = isset( $args[0] ) ? $args[0] : 'claude/admiring-tesla-goowtl'; // pass a commit SHA to bypass GitHub's raw CDN cache
$getfit_base = 'https://raw.githubusercontent.com/gajula-atarim/Personal-Trainer/' . $getfit_ref . '/';

$getfit_get = function ( $path ) use ( $getfit_base ) {
	$res = wp_remote_get( $getfit_base . $path . '?nocache=' . time(), array( 'timeout' => 30 ) );
	if ( is_wp_error( $res ) || 200 !== (int) wp_remote_retrieve_response_code( $res ) ) {
		WP_CLI::error( 'Could not fetch ' . $path );
	}
	return wp_remote_retrieve_body( $res );
};

$getfit_json = function ( $path ) use ( $getfit_get ) {
	$body = $getfit_get( $path );
	$data = json_decode( $body, true );
	if ( null === $data ) {
		WP_CLI::error( 'Invalid JSON in ' . $path );
	}
	return array( $body, $data );
};

$getfit_upsert = function ( $type, $slug, $title, $json, $meta ) {
	$post = get_page_by_path( $slug, OBJECT, $type );
	$id   = $post ? $post->ID : wp_insert_post(
		array(
			'post_type'   => $type,
			'post_name'   => $slug,
			'post_title'  => $title,
			'post_status' => 'publish',
		),
		true
	);
	if ( is_wp_error( $id ) ) {
		WP_CLI::error( $id->get_error_message() );
	}
	if ( $post && 'publish' !== $post->post_status ) {
		wp_update_post( array( 'ID' => $id, 'post_status' => 'publish' ) );
	}
	update_post_meta( $id, '_elementor_edit_mode', 'builder' );
	update_post_meta( $id, '_elementor_version', ELEMENTOR_VERSION );
	update_post_meta( $id, '_elementor_data', wp_slash( $json ) );
	foreach ( $meta as $key => $value ) {
		update_post_meta( $id, $key, $value );
	}
	foreach ( array( '_elementor_css', '_elementor_element_cache', '_elementor_page_assets' ) as $key ) {
		delete_post_meta( $id, $key );
	}
	return (int) $id;
};

// 1. Site Settings (Elementor kit).
$getfit_kit_id = (int) get_option( 'elementor_active_kit' );
list( , $getfit_kit ) = $getfit_json( 'elementor/kit.json' );
$getfit_kit_old = get_post_meta( $getfit_kit_id, '_elementor_page_settings', true );
update_post_meta( $getfit_kit_id, '_elementor_page_settings', array_merge( is_array( $getfit_kit_old ) ? $getfit_kit_old : array(), $getfit_kit ) );
delete_post_meta( $getfit_kit_id, '_elementor_css' );

// 2. UAE header + footer, shown on the entire site.
$getfit_rules = array(
	'rule'     => array( 'basic-global' ),
	'specific' => array(),
);
list( $getfit_header ) = $getfit_json( 'elementor/header.json' );
list( $getfit_footer ) = $getfit_json( 'elementor/footer.json' );
$getfit_header_id = $getfit_upsert(
	'elementor-hf',
	'getfit-header',
	'Get Fit Header',
	$getfit_header,
	array(
		'_elementor_template_type'     => 'wp-post',
		'ehf_template_type'            => 'type_header',
		'ehf_target_include_locations' => $getfit_rules,
		'ehf_target_exclude_locations' => array(),
		'ehf_target_user_roles'        => array( 'all' ),
	)
);
$getfit_footer_id = $getfit_upsert(
	'elementor-hf',
	'getfit-footer',
	'Get Fit Footer',
	$getfit_footer,
	array(
		'_elementor_template_type'     => 'wp-post',
		'ehf_template_type'            => 'type_footer',
		'ehf_target_include_locations' => $getfit_rules,
		'ehf_target_exclude_locations' => array(),
		'ehf_target_user_roles'        => array( 'all' ),
	)
);

// 3. Home page as the static front page.
list( $getfit_home ) = $getfit_json( 'elementor/home.json' );
$getfit_home_id = $getfit_upsert(
	'page',
	'home',
	'Home',
	$getfit_home,
	array(
		'_elementor_template_type' => 'wp-page',
		'_wp_page_template'        => 'elementor_header_footer',
		'_elementor_page_settings' => array( 'hide_title' => 'yes' ),
	)
);
update_option( 'show_on_front', 'page' );
update_option( 'page_on_front', $getfit_home_id );

// 4. Design layer (child theme assets/).
update_option( 'getfit_css', $getfit_get( 'wp-content/themes/getfit-child/assets/css/getfit.css' ), false );
update_option( 'getfit_js', $getfit_get( 'wp-content/themes/getfit-child/assets/js/getfit.js' ), false );
if ( empty( $assoc_args['skip-files'] ) ) {
	// Same code as theme files (what `wp getfit export-assets` does).
	foreach ( array( 'css/getfit.css' => 'getfit_css', 'js/getfit.js' => 'getfit_js' ) as $getfit_rel => $getfit_opt ) {
		$getfit_file = get_stylesheet_directory() . '/assets/' . $getfit_rel;
		wp_mkdir_p( dirname( $getfit_file ) );
		file_put_contents( $getfit_file, get_option( $getfit_opt ) ); // phpcs:ignore WordPress.WP.AlternativeFunctions
	}
}

// 5. Rebuild Elementor CSS.
\Elementor\Plugin::$instance->files_manager->clear_cache();

WP_CLI::success(
	wp_json_encode(
		array(
			'kit'    => $getfit_kit_id,
			'header' => $getfit_header_id,
			'footer' => $getfit_footer_id,
			'home'   => $getfit_home_id,
		)
	)
);
