"""Finnish copy for the PersonalTrainer build (English source string -> Finnish).

gen.py applies this to every visible text setting when it builds the JSON,
so the English page definitions in page.py / hf.py stay the single source of
layout and the language lives here.
"""

FI = {
    # hero
    'Strength · Kamppi studio': 'Voima · Kampin studio',
    'Get strong.<br><span class="gf-lime">Stay strong.</span>': 'Vahvistu.<br><span class="gf-lime">Pysy vahvana.</span>',
    '<p>Coached personal training in central Helsinki. A plan built for your body, technique checked every session, progress you can measure.</p>':
        '<p>Henkilökohtaista valmennusta Helsingin keskustassa. Kehollesi tehty ohjelma, tekniikka tarkistetaan joka kerta ja edistyminen näkyy mittareissa.</p>',
    'Book a free trial': 'Varaa ilmainen kokeilu',
    'How it works': 'Näin se toimii',
    '<span class="gf-stars">★★★★★</span><strong>4.9</strong> from 380+ reviews': '<span class="gf-stars">★★★★★</span><strong>4,9</strong> yli 380 arvostelusta',
    'Certified, insured coaches': 'Sertifioidut, vakuutetut valmentajat',
    'No contract, cancel anytime': 'Ei sitoutumista, peru milloin vain',
    'Weight loss · Training + nutrition': 'Painonpudotus · Treeni + ravinto',
    'Lose the weight.<br><span class="gf-lime">For good.</span>': 'Pudota painoa.<br><span class="gf-lime">Pysyvästi.</span>',
    '<p>Training, nutrition and weekly check-ins in one plan you can keep — long after the first month.</p>':
        '<p>Treeni, ravinto ja viikoittaiset seurannat yhdessä ohjelmassa, jossa pysyt mukana – vielä kauan ensimmäisen kuukauden jälkeen.</p>',
    'Online coaching · Anywhere': 'Etävalmennus · Missä vain',
    'Your coach.<br><span class="gf-lime">In your pocket.</span>': 'Valmentaja.<br><span class="gf-lime">Taskussasi.</span>',
    '<p>A programme in the app, video form reviews and a real coach checking in every week, wherever you train.</p>':
        '<p>Ohjelma sovelluksessa, tekniikkapalaute videolta ja oikea valmentaja, joka pitää yhteyttä joka viikko – treenasitpa missä tahansa.</p>',
    '01 · Strength': '01 · Voima',
    '02 · Weight loss': '02 · Painonpudotus',
    '03 · Online coaching': '03 · Etävalmennus',

    # studio
    'Inside the studio': 'Studiollamme',
    'Transform your workout.': 'Uudista treenisi.',
    '<p>A private studio in Kamppi with everything you need to train well — and nothing you don’t.</p>':
        '<p>Yksityinen studio Kampissa – kaikki mitä hyvään treeniin tarvitset, eikä mitään turhaa.</p>',
    'Quality equipment': 'Laadukkaat välineet',
    '<p>Racks, free weights and conditioning kit maintained to a high standard.</p>': '<p>Telineet, vapaat painot ja kuntoiluvälineet huolellisesti ylläpidettyinä.</p>',
    'Spotless & private': 'Siisti ja rauhallinen',
    '<p>Cleaned between every session, with a limited number of clients on the floor.</p>': '<p>Siivotaan jokaisen treenin välissä, ja salilla on kerrallaan vain muutama asiakas.</p>',
    'Showers & lockers': 'Suihkut ja kaapit',
    '<p>Fresh towels, showers and secure lockers so you can train before work.</p>': '<p>Puhtaat pyyhkeet, suihkut ja lukittavat kaapit – ehdit hyvin treenata ennen töitä.</p>',
    'Nutrition plan': 'Ravinto-ohjelma',
    '<p>Clear calorie and protein targets with meals you actually enjoy eating.</p>': '<p>Selkeät kalori- ja proteiinitavoitteet ja ateriat, joista oikeasti pidät.</p>',
    'Discover more about us': 'Tutustu meihin',

    # about
    'About PersonalTrainer': 'Tietoa PersonalTrainerista',
    'Built by Oliver Virtanen, for people done with starting over.': 'Oliver Virtasen luoma – niille, jotka ovat kyllästyneet aloittamaan alusta.',
    '<p>Oliver has coached in Helsinki for twelve years. He started PersonalTrainer to give busy people what most gyms don’t: a real coach, a plan written for them and someone checking in every week.</p>':
        '<p>Oliver on valmentanut Helsingissä kaksitoista vuotta. Hän perusti PersonalTrainerin antaakseen kiireisille ihmisille sen, mitä useimmat salit eivät anna: oikean valmentajan, juuri heille kirjoitetun ohjelman ja jonkun, joka kysyy kuulumiset joka viikko.</p>',
    '<p>Today he leads a team of certified coaches in Kamppi and online — with the same no-shortcuts approach.</p>':
        '<p>Nykyään hän johtaa sertifioitujen valmentajien tiimiä Kampissa ja verkossa – samalla oikoteitä välttävällä otteella.</p>',
    'Certified Strength & Conditioning Specialist': 'Sertifioitu voima- ja kuntovalmentaja (CSCS)',
    'Precision Nutrition Level 1': 'Precision Nutrition, taso 1',
    'BSc Sports Science, University of Jyväskylä': 'Liikuntatieteiden kandidaatti, Jyväskylän yliopisto',
    'Explore our plans →': 'Katso paketit →',
    '<p>“I’d tried three gyms before PersonalTrainer. Oliver’s team was the first to make it feel personal — and the first that stuck.”</p>':
        '<p>”Kokeilin kolmea salia ennen PersonalTraineria. Oliverin tiimi oli ensimmäinen, jolla treeni tuntui henkilökohtaiselta – ja ensimmäinen, jossa pysyin mukana.”</p>',
    'Client since 2024 · Helsinki': 'Asiakas vuodesta 2024 · Helsinki',

    # problems
    '01 · Sound familiar?': '01 · Kuulostaako tutulta?',
    'You’ve started before. Here’s why it didn’t stick.': 'Olet aloittanut ennenkin. Tästä syystä se ei jäänyt pysyväksi.',
    '<p>Most people don’t fail for lack of willpower. They fail because the plan was never built for them.</p>':
        '<p>Harva epäonnistuu tahdonvoiman puutteeseen. Useimmiten ohjelmaa ei vain koskaan tehty juuri heille.</p>',
    'A generic plan': 'Geneerinen ohjelma',
    '<p>Copied from an app or a friend, ignoring your body, your schedule and your goal.</p>': '<p>Kopioitu sovelluksesta tai kaverilta – kehoasi, aikatauluasi ja tavoitettasi huomioimatta.</p>',
    'Nobody checking in': 'Kukaan ei seuraa',
    '<p>Motivation drops in week three and there’s no one to notice, adjust or push.</p>': '<p>Motivaatio hiipuu kolmannella viikolla, eikä kukaan huomaa, korjaa suuntaa tai kannusta.</p>',
    'Crash diets': 'Pikadieetit',
    '<p>They work for a month, then the weight comes back — and so does the frustration.</p>': '<p>Ne toimivat kuukauden, sitten paino palaa – ja turhautuminen sen mukana.</p>',
    'PersonalTrainer fixes all three. <a href="#method">Here’s how ↓</a>': 'PersonalTrainer korjaa kaikki kolme. <a href="#method">Näin se toimii ↓</a>',

    # method
    '02 · The PersonalTrainer method': '02 · PersonalTrainer-menetelmä',
    'A coach, a plan and a check-in <span class="gf-lime">every week.</span>': 'Valmentaja, ohjelma ja seuranta <span class="gf-lime">joka viikko.</span>',
    '<p>One coach walks with you from your free trial to results that last.</p>': '<p>Sama valmentaja kulkee rinnallasi ilmaisesta kokeilusta pysyviin tuloksiin.</p>',
    'Day 1': 'Päivä 1',
    'Free trial': 'Ilmainen kokeilu',
    '<p>Train with a coach, get a movement assessment and set a clear goal together.</p>': '<p>Treenaa valmentajan kanssa, saat liikkuvuusarvion ja asetatte yhdessä selkeän tavoitteen.</p>',
    'Within 48 hours': '48 tunnin sisällä',
    'Your plan': 'Oma ohjelma',
    '<p>Training and nutrition built around your body, schedule and food you enjoy.</p>': '<p>Treeni ja ravinto suunniteltuna kehosi, aikataulusi ja lempiruokiesi mukaan.</p>',
    '2–3× a week': '2–3 × viikossa',
    'Coached sessions': 'Valmennetut treenit',
    '<p>In our Kamppi studio or online, with technique and load checked every time.</p>': '<p>Kampin studiollamme tai etänä – tekniikka ja kuormat tarkistetaan joka kerta.</p>',
    'Every week': 'Joka viikko',
    'Check-in': 'Seuranta',
    '<p>We review your progress and update the plan so you never stall.</p>': '<p>Käymme edistymisesi läpi ja päivitämme ohjelmaa, jotta kehitys ei pysähdy.</p>',

    # programmes
    '03 · Choose your path': '03 · Valitse suuntasi',
    'One goal. The right programme for it.': 'Yksi tavoite. Oikea ohjelma sen saavuttamiseen.',
    'Not sure? Ask in your free trial': 'Epävarma? Kysy ilmaisessa kokeilussa',
    '01 · Best for building strength': '01 · Paras voiman kasvattamiseen',
    'Strength Foundations': 'Voimaperusta',
    '<p>Master the big lifts and get measurably stronger in 12 weeks, 2–3 studio sessions a week.</p>': '<p>Opettele päänostot ja vahvistu mitattavasti 12 viikossa, 2–3 studiotreeniä viikossa.</p>',
    '02 · Best for fat loss': '02 · Paras rasvanpudotukseen',
    'Body Recomposition': 'Kehonmuokkaus',
    '<p>Lose fat, keep your muscle. Training, nutrition targets and weekly weigh-ins in one plan.</p>': '<p>Rasva pois, lihakset säilyvät. Treeni, ravintotavoitteet ja viikoittaiset punnitukset yhdessä ohjelmassa.</p>',
    '03 · Best for busy schedules': '03 · Paras kiireisille',
    'Online Coaching': 'Etävalmennus',
    '<p>Train anywhere with a weekly-updated programme, form reviews within 24 hours and direct chat.</p>': '<p>Treenaa missä vain: viikoittain päivittyvä ohjelma, tekniikkapalaute 24 tunnissa ja suora chat.</p>',

    # results
    '04 · The proof': '04 · Tulokset',
    'Real people. Busy lives. Results that last.': 'Oikeita ihmisiä. Kiireisiä arkia. Pysyviä tuloksia.',
    'clients coached in Helsinki and online': 'valmennettua asiakasta Helsingissä ja etänä',
    'average rating from 380+ reviews': 'keskiarvo yli 380 arvostelusta',
    'still training with us after 6 months': 'treenaa kanssamme yhä 6 kuukauden jälkeen',
    'average fat loss in 16 weeks': 'keskimääräinen rasvanpudotus 16 viikossa',
    'in 20 weeks': '20 viikossa',
    '<p><strong>Mikko, 41</strong> · <span class="gf-soft">Body Recomposition</span></p>': '<p><strong>Mikko, 41</strong> · <span class="gf-soft">Kehonmuokkaus</span></p>',
    'on his deadlift in 6 months': 'maastavetoon 6 kuukaudessa',
    '<p><strong>Jussi, 34</strong> · <span class="gf-soft">Strength Foundations</span></p>': '<p><strong>Jussi, 34</strong> · <span class="gf-soft">Voimaperusta</span></p>',
    'in 16 weeks, fully online': '16 viikossa, täysin etänä',
    '<p><strong>Daniel, 29</strong> · <span class="gf-soft">Online Coaching</span></p>': '<p><strong>Daniel, 29</strong> · <span class="gf-soft">Etävalmennus</span></p>',
    '<p>“I know exactly what to do every session and why. Six months in and I’m stronger than I’ve ever been.”</p>':
        '<p>”Tiedän joka treenissä tarkalleen mitä teen ja miksi. Puolen vuoden jälkeen olen vahvempi kuin koskaan.”</p>',
    'Strength Foundations · Verified client': 'Voimaperusta · Vahvistettu asiakas',
    '<p>“Fourteen kilos down without feeling like I’m on a diet. The weekly check-ins kept me honest.”</p>':
        '<p>”Neljätoista kiloa pois ilman dieettifiilistä. Viikoittaiset seurannat pitivät minut rehellisenä.”</p>',
    'Body Recomposition · Verified client': 'Kehonmuokkaus · Vahvistettu asiakas',
    '<p>“I travel constantly for work and still haven’t missed a week. The app and form reviews are brilliant.”</p>':
        '<p>”Matkustan jatkuvasti työn takia, enkä silti ole jättänyt väliin yhtään viikkoa. Sovellus ja tekniikkapalaute ovat loistavia.”</p>',
    'Online Coaching · Verified client': 'Etävalmennus · Vahvistettu asiakas',
    '<p>“My back pain is gone and I squat more than ever. Calm, precise coaching that actually cares.”</p>':
        '<p>”Selkäkivut ovat poissa ja kyykkään enemmän kuin koskaan. Rauhallista ja tarkkaa valmennusta, joka oikeasti välittää.”</p>',
    'Studio plan · Verified client': 'Studiopaketti · Vahvistettu asiakas',
    '<p>“The free trial sold me. I left with a real plan and a coach who remembered my name the next week.”</p>':
        '<p>”Ilmainen kokeilu vakuutti minut. Lähdin kotiin oikean ohjelman kanssa, ja valmentaja muisti nimeni vielä seuraavalla viikolla.”</p>',
    'Intensive plan · Verified client': 'Intensiivipaketti · Vahvistettu asiakas',
    '<p>“First gym I’ve stuck with for more than two months. It feels personal, never intimidating.”</p>':
        '<p>”Ensimmäinen sali, jossa olen pysynyt yli kaksi kuukautta. Tunnelma on henkilökohtainen eikä koskaan pelottava.”</p>',

    # coaches
    '05 · Your coaches': '05 · Valmentajamme',
    'Experts who care whether you show up.': 'Asiantuntijat, joille on väliä, että tulet paikalle.',
    '<p>Every PersonalTrainer coach is certified, insured and has at least five years of hands-on coaching.</p>':
        '<p>Jokainen PersonalTrainer-valmentaja on sertifioitu ja vakuutettu, ja jokaisella on vähintään viiden vuoden valmennuskokemus.</p>',
    'Strength & conditioning': 'Voima- ja kuntovalmennus',
    'CSCS · 9 years coaching': 'CSCS · 9 vuotta valmentajana',
    'Weight loss & nutrition': 'Painonpudotus ja ravinto',
    'Precision Nutrition L2 · 7 years': 'Precision Nutrition L2 · 7 vuotta',
    'Online coaching': 'Etävalmennus',
    'BSc Sports Science · 6 years': 'LitK · 6 vuotta',
    'Mobility & rehab': 'Liikkuvuus ja kuntoutus',
    'Physiotherapist · 8 years': 'Fysioterapeutti · 8 vuotta',

    # pricing
    '06 · Pricing': '06 · Hinnasto',
    'Simple plans. Zero risk to start.': 'Selkeät paketit. Aloitus ilman riskiä.',
    '<span class="gf-offer-tag">OFFER</span>50% off your first month — until 30 November': '<span class="gf-offer-tag">TARJOUS</span>Ensimmäinen kuukausi −50 % – 30.11. asti',
    'Monthly': 'Kuukausittain',
    '3 months · save 10%': '3 kk · säästä 10 %',
    'Online package': 'Etäpaketti',
    'Remote coaching, any gym': 'Etävalmennus, mikä tahansa sali',
    '€129': '129 €',
    '€299': '299 €',
    '€529': '529 €',
    '€85': '85 €',
    '€60': '60 €',
    '/ month': '/ kk',
    'Billed monthly · cancel anytime': 'Laskutus kuukausittain · peru milloin vain',
    'Personal programme in the app': 'Henkilökohtainen ohjelma sovelluksessa',
    'Weekly check-in & adjustments': 'Viikoittainen seuranta ja säädöt',
    'Video form reviews': 'Tekniikkapalaute videolta',
    'Chat with your coach': 'Chat valmentajan kanssa',
    'Choose plan': 'Valitse paketti',
    'Studio package': 'Studiopaketti',
    'Popular': 'Suosituin',
    '4 coached sessions a month': '4 valmennettua treeniä kuukaudessa',
    '4 × 60 min studio sessions': '4 × 60 min studiotreeniä',
    'Everything in Online': 'Kaikki Etäpaketin sisältö',
    'Personal nutrition plan': 'Henkilökohtainen ravinto-ohjelma',
    'Monthly progress review': 'Kuukausittainen edistymisen arviointi',
    'Intensive package': 'Intensiivipaketti',
    '8 coached sessions a month': '8 valmennettua treeniä kuukaudessa',
    '8 × 60 min studio sessions': '8 × 60 min studiotreeniä',
    'Everything in Studio': 'Kaikki Studiopaketin sisältö',
    'Body composition scans': 'Kehonkoostumusmittaukset',
    'Priority booking': 'Etusija varauksissa',
    'First session free': 'Ensimmäinen treeni ilmaiseksi',
    'No lock-in contract': 'Ei määräaikaista sopimusta',
    'Pause up to 4 weeks a year': 'Tauko jopa 4 viikkoa vuodessa',
    'Secure payment': 'Turvallinen maksu',

    # booking
    '07 · Your first step': '07 · Ensimmäinen askel',
    'Book your free trial in 60 seconds.': 'Varaa ilmainen kokeilu 60 sekunnissa.',
    'Choose a session': 'Valitse treeni',
    'Pick date & time': 'Päivä ja aika',
    'Your details': 'Omat tiedot',
    'Confirmed': 'Vahvistettu',
    'Step 1 of 3': 'Vaihe 1/3',
    'Free trial session': 'Ilmainen kokeilutreeni',
    '45 min · Studio or video': '45 min · Studio tai video',
    'Free': 'Ilmainen',
    '1:1 Strength Session': 'Henkilökohtainen voimatreeni',
    '60 min · Studio': '60 min · Studio',
    'Online Coaching Kick-off': 'Etävalmennuksen aloitus',
    '45 min · Video call': '45 min · Videopuhelu',
    'Step 2 of 3': 'Vaihe 2/3',
    'Pick a date & time': 'Valitse päivä ja aika',
    'Step 3 of 3': 'Vaihe 3/3',
    'You’re in, <span class="gf-first-name">friend</span>.': 'Tervetuloa, <span class="gf-first-name">ystävä</span>!',
    '<p><span class="gf-done-service">Your session</span> on <span class="gf-done-date"></span> at <span class="gf-done-time"></span>. Your coach will confirm by email at <span class="gf-done-email"></span> within the hour.</p>':
        '<p><span class="gf-done-service">Treenisi</span>: <span class="gf-done-date"></span> klo <span class="gf-done-time"></span>. Valmentajasi vahvistaa varauksen tunnin sisällä sähköpostiin <span class="gf-done-email"></span>.</p>',
    'Book another session': 'Varaa toinen treeni',
    '← Back': '← Takaisin',
    'Continue': 'Jatka',

    # faq
    '08 · Questions': '08 · Kysymykset',
    'Still deciding? Good questions.': 'Vielä mietinnässä? Hyviä kysymyksiä.',
    '<p>Anything else, email <a href="mailto:example@example-personal-trainer.com">example@example-personal-trainer.com</a>. We reply within one working day.</p>':
        '<p>Muuta kysyttävää? Lähetä viesti osoitteeseen <a href="mailto:example@example-personal-trainer.com">example@example-personal-trainer.com</a>. Vastaamme yhden arkipäivän kuluessa.</p>',
    'I’m a complete beginner. Is this for me?': 'Olen täysin aloittelija. Sopiiko tämä minulle?',
    'What happens in the free trial?': 'Mitä ilmaisessa kokeilussa tapahtuu?',
    'How does online coaching work?': 'Miten etävalmennus toimii?',
    'Is there a contract?': 'Onko sopimus määräaikainen?',
    'Can I pause my plan?': 'Voinko pitää taukoa?',
    '<p>Yes. Most of our clients start with little or no gym experience. Your free trial includes a movement assessment, and the plan starts exactly where you are.</p>':
        '<p>Sopii. Useimmilla asiakkaillamme on aloittaessa vähän tai ei lainkaan salikokemusta. Ilmaiseen kokeiluun kuuluu liikkuvuusarvio, ja ohjelma aloitetaan juuri sinun tasoltasi.</p>',
    '<p>45 minutes with a coach: a short chat about your goal, a movement assessment and a real workout. You leave with a recommended plan — no obligation to join.</p>':
        '<p>45 minuuttia valmentajan kanssa: lyhyt keskustelu tavoitteestasi, liikkuvuusarvio ja oikea treeni. Saat mukaasi suositellun ohjelman – ilman velvoitetta liittyä.</p>',
    '<p>Your programme lives in the app and is updated weekly. Film key lifts for form feedback within 24 hours, chat with your coach any time, and join a monthly video review.</p>':
        '<p>Ohjelmasi on sovelluksessa ja päivittyy viikoittain. Kuvaa tärkeimmät liikkeet ja saat tekniikkapalautteen 24 tunnissa, juttele valmentajan kanssa milloin vain ja osallistu kuukausittaiseen videopalaveriin.</p>',
    '<p>No. Plans are billed monthly and you can cancel any time. Sessions can be moved free of charge up to 24 hours before.</p>':
        '<p>Ei ole. Paketit laskutetaan kuukausittain ja voit perua milloin tahansa. Treenin voi siirtää maksutta viimeistään 24 tuntia ennen.</p>',
    '<p>Yes, up to four weeks a year for holidays or illness, at no cost.</p>':
        '<p>Voit, jopa neljä viikkoa vuodessa lomien tai sairastumisen vuoksi – maksutta.</p>',

    # final CTA
    '09 · Your move': '09 · Sinun vuorosi',
    'Stop wishing.<br><span class="gf-lime">Start training.</span>': 'Lopeta haaveilu.<br><span class="gf-lime">Aloita treeni.</span>',
    '<p>Your first session is free. If it’s not for you, you walk away with a plan anyway.</p>':
        '<p>Ensimmäinen treeni on ilmainen. Jos se ei tunnu omalta, saat silti ohjelman mukaasi.</p>',
    'Book a free trial →': 'Varaa ilmainen kokeilu →',
    'Only 6 trial slots left this week': 'Tällä viikolla vain 6 kokeiluaikaa jäljellä',

    # footer
    'Ready when you are.': 'Valmiina, kun sinä olet.',
    '<p>Your first session is free. No contract, no pressure.</p>': '<p>Ensimmäinen treeni on ilmainen. Ei sopimusta, ei painostusta.</p>',
    'Call +358 40 123 4567': 'Soita +358 40 123 4567',
    '<p>Personal training in central Helsinki and online. Strength, weight loss and coaching that fits your life.</p>':
        '<p>Henkilökohtaista valmennusta Helsingin keskustassa ja etänä. Voimaa, painonpudotusta ja valmennusta, joka sopii elämääsi.</p>',
    'Explore': 'Selaa',
    'About': 'Meistä',
    'Programmes': 'Ohjelmat',
    'Pricing': 'Hinnasto',
    'FAQ': 'UKK',
    'Visit': 'Käy luonamme',
    '<p>Urho Kekkosen katu 1<br>00100 Helsinki, Finland</p>': '<p>Urho Kekkosen katu 1<br>00100 Helsinki</p>',
    'Get directions ↗': 'Reittiohjeet ↗',
    '<p>Mon–Fri 06:30 – 20:00<br>Sat 08:00 – 14:00</p>': '<p>Ma–pe 6.30–20.00<br>La 8.00–14.00</p>',
    'Contact': 'Yhteystiedot',
    'Coach with us': 'Valmentajaksi meille',
    '© [hfe_current_year] PersonalTrainer. All rights reserved.': '© [hfe_current_year] PersonalTrainer. Kaikki oikeudet pidätetään.',
    'Privacy': 'Tietosuoja',
    'Terms': 'Käyttöehdot',
    'Back to top <span class="gf-totop">↑</span>': 'Takaisin ylös <span class="gf-totop">↑</span>',
}

# Booking form (HTML widgets).
FI_HTML = {
    '<div class="gf-days" aria-label="Choose a day"></div><div class="gf-times-label">Available times</div><div class="gf-times" aria-label="Choose a time"></div><div class="gf-times-empty">Select a day to see open slots.</div>':
        '<div class="gf-days" aria-label="Valitse päivä"></div><div class="gf-times-label">Vapaat ajat</div><div class="gf-times" aria-label="Valitse aika"></div><div class="gf-times-empty">Valitse päivä nähdäksesi vapaat ajat.</div>',
    '<div class="gf-summary"><div class="gf-summary-name"></div><div class="gf-summary-when"></div></div><form class="gf-form" novalidate><label>Full name<input name="name" autocomplete="name" placeholder="Aino Laine"></label><label>Email<input name="email" type="email" autocomplete="email" placeholder="you@example.com"></label><label>What would you like to achieve? <span>Optional</span><textarea name="note" rows="3" placeholder="e.g. Lose 8 kg before summer"></textarea></label></form>':
        '<div class="gf-summary"><div class="gf-summary-name"></div><div class="gf-summary-when"></div></div><form class="gf-form" novalidate><label>Koko nimi<input name="name" autocomplete="name" placeholder="Aino Laine"></label><label>Sähköposti<input name="email" type="email" autocomplete="email" placeholder="nimi@esimerkki.fi"></label><label>Mitä haluaisit saavuttaa? <span>Vapaaehtoinen</span><textarea name="note" rows="3" placeholder="esim. −8 kg ennen kesää"></textarea></label></form>',
}

# Counter suffixes: Finnish puts a (non-breaking) space before % and units.
FI_SUFFIX = {'%': '\u00a0%', ' kg': '\u00a0kg'}

# Site Settings (Elementor kit).
FI_KIT = {'site_description': 'Henkilökohtaista valmennusta Helsingissä ja etänä'}
