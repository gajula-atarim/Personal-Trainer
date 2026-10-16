<?php
/**
 * Get Fit child theme for Hello Elementor.
 *
 * Page content lives in Elementor (header and footer are UAE templates). This
 * theme only adds the design layer Elementor has no control for: scroll
 * reveals, the hero slider, method steps, testimonial marquee, booking flow,
 * header scroll state and the dumbbell cursor.
 *
 * @package GetFitChild
 */

defined( 'ABSPATH' ) || exit;

define( 'GETFIT_CHILD_VERSION', '1.0.0' );

/**
 * Enqueue parent + child styles and the Get Fit design assets.
 *
 * assets/css/getfit.css and assets/js/getfit.js are the source of truth. While
 * they do not exist yet (first build), the same code is read from the
 * getfit_css / getfit_js options so it can be tuned without file access.
 */
function getfit_child_enqueue() {
	$dir = get_stylesheet_directory();
	$uri = get_stylesheet_directory_uri();

	wp_enqueue_style( 'hello-elementor-parent', get_template_directory_uri() . '/style.css', array(), wp_get_theme( 'hello-elementor' )->get( 'Version' ) );
	wp_enqueue_style( 'getfit-child', get_stylesheet_uri(), array( 'hello-elementor-parent' ), GETFIT_CHILD_VERSION );

	$css_file = $dir . '/assets/css/getfit.css';
	if ( file_exists( $css_file ) ) {
		wp_enqueue_style( 'getfit', $uri . '/assets/css/getfit.css', array( 'getfit-child' ), filemtime( $css_file ) );
	} else {
		wp_register_style( 'getfit', false, array( 'getfit-child' ), GETFIT_CHILD_VERSION );
		wp_enqueue_style( 'getfit' );
		wp_add_inline_style( 'getfit', (string) get_option( 'getfit_css', '' ) );
	}

	$js_file = $dir . '/assets/js/getfit.js';
	if ( file_exists( $js_file ) ) {
		wp_enqueue_script( 'getfit', $uri . '/assets/js/getfit.js', array(), filemtime( $js_file ), array( 'in_footer' => true ) );
	} else {
		wp_register_script( 'getfit', false, array(), GETFIT_CHILD_VERSION, array( 'in_footer' => true ) );
		wp_enqueue_script( 'getfit' );
		wp_add_inline_script( 'getfit', (string) get_option( 'getfit_js', '' ) );
	}
}
add_action( 'wp_enqueue_scripts', 'getfit_child_enqueue', 20 );

/**
 * Body class used to scope all Get Fit styles.
 */
add_filter(
	'body_class',
	function ( $classes ) {
		$classes[] = 'getfit';
		return $classes;
	}
);

/**
 * `wp getfit export-assets` writes the getfit_css / getfit_js options into
 * assets/css/getfit.css and assets/js/getfit.js.
 */
if ( defined( 'WP_CLI' ) && WP_CLI ) {
	WP_CLI::add_command(
		'getfit export-assets',
		function () {
			$dir   = get_stylesheet_directory() . '/assets';
			$files = array(
				'css/getfit.css' => (string) get_option( 'getfit_css', '' ),
				'js/getfit.js'   => (string) get_option( 'getfit_js', '' ),
			);
			foreach ( $files as $rel => $code ) {
				if ( '' === trim( $code ) ) {
					WP_CLI::warning( "Option for {$rel} is empty, skipped." );
					continue;
				}
				wp_mkdir_p( dirname( $dir . '/' . $rel ) );
				file_put_contents( $dir . '/' . $rel, $code ); // phpcs:ignore WordPress.WP.AlternativeFunctions
				WP_CLI::log( "Wrote assets/{$rel} (" . strlen( $code ) . ' bytes)' );
			}
			WP_CLI::success( 'Get Fit assets exported.' );
		}
	);
}
