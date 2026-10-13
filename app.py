import html

import streamlit as st


# PERSONAL CONTENT CONFIGURATION
# Edit names, titles, and messages together here.
PERSONAL_CONTENT = {
    "website_title": "Project Cupid — A Little World for Rashi",
    "recipient_full_name": "Rashi Sharma",
    "recipient": "Rashi",
    "sender": "Shreshth Gupta",
    "topline_note": "A little world made with all my love",
    "hero_eyebrow": "For Rashi, with love",
    "begin_button": "Come on in, Rashi",
    "seal_top": "For",
    "seal_bottom": "Rashi",
    "note_label": "A note for {recipient}",
    "headline": "Rashi, you make life a little more beautiful.",
    "subtitle": "A small world made just for you, to celebrate the person I adore and the joy you bring simply by being yourself.",
    "welcome_note": "Rashi, I love your kindness, your spirit, and the way you make the world feel brighter. I feel lucky to love you, and I hope this little corner reminds you how cherished you are.",
    "reasons_section": {
        "eyebrow": "A few little things",
        "title": "Reasons I adore you, Rashi.",
        "intro": "Little things about you that make my heart feel very full.",
        "reason_label": "A small reminder {number}",
        "open_button": "Read this reason",
        "close_button": "Close this reason",
        "reasons": [
            {
                "title": "Your kind heart",
                "detail": "The kindness and care you bring into the world say so much about the beautiful person you are.",
            },
            {
                "title": "Your unmistakable light",
                "detail": "I love your spirit and your point of view; there is no one else quite like you, Rashi.",
            },
            {
                "title": "Simply being you",
                "detail": "You do not have to be anything more than yourself to be loved completely. I adore you exactly as you are.",
            },
        ],
    },
    "letter": {
        "eyebrow": "A letter from {sender}",
        "title": "For my dear Rashi.",
        "intro": "",
        "open_button": "Open your letter, Rashi",
        "salutation": "Dear {recipient},",
        "paragraphs": [
            "Rashi, I want you to know how grateful I am for you. The person you are brings so much warmth into the world, and I feel lucky to love you.",
            "Your kindness, your perspective, and the way you are wonderfully yourself are all things I treasure. I hope you always feel appreciated, supported, and free to be exactly who you are.",
            "Please keep this close: you are precious to me, I believe in you, and I love you for all that you are.",
        ],
        "signoff": "With love, Shreshth ❤️",
    },
    "question": {
        "eyebrow": "One tiny question",
        "title": "Rashi, may I make your day a little sweeter?",
        "intro": "Pick whichever answer makes you smile. No pressure, and no wrong choices.",
        "options": [
            {
                "label": "Yes, please",
                "reply": "Then here is a little reminder from Shreshth: I adore you, Rashi, exactly as you are.",
            },
            {
                "label": "Only with a compliment",
                "reply": "Deal: you are thoughtful, bright, and wonderfully one of a kind. That is one of the many things I love about you.",
            },
        ],
    },
    "surprise": {
        "eyebrow": "One last note from Shreshth",
        "title": "Rashi, I saved one last little thing for you.",
        "button": "Open your surprise, Rashi",
        "revealed_title": "My favorite thing is you.",
        "message": "Rashi, no matter how many words I put on this page, the simplest truth stays the same: I love you, and I am so glad you are you.",
        "signoff": "Always with love, Shreshth ❤️",
    },
    "footer": "A little world for Rashi Sharma, made with love by Shreshth Gupta.",
}

st.set_page_config(
    page_title=PERSONAL_CONTENT["website_title"],
    page_icon="♥",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    :root {
        --cream: #fffaf4;
        --paper: #fffdf9;
        --rose: #a84f68;
        --rose-dark: #77374c;
        --blush: #f7e4e5;
        --lavender: #eee8f2;
        --ink: #382c30;
        --muted: #76666a;
        --line: rgba(119, 55, 76, 0.16);
    }

    html {
        scroll-behavior: smooth;
        scroll-padding-top: 2rem;
    }

    body, [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(ellipse at 88% 18%, rgba(238, 232, 242, 0.62), transparent 30rem),
            radial-gradient(ellipse at 8% 44%, rgba(247, 228, 229, 0.58), transparent 34rem),
            var(--cream);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer {
        display: none !important;
    }

    .block-container {
        max-width: 1240px;
        padding: 1.15rem clamp(1.1rem, 5vw, 4.5rem) 3rem;
    }

    .topline,
    .hero .hero-subtitle,
    .hero .eyebrow,
    .note .note-label,
    .section-kicker,
    .section-intro,
    .reason-index,
    .reason-copy,
    .letter-body,
    .letter-signoff,
    .question-reply,
    .surprise-copy,
    .footer-note { font-family: 'DM Sans', sans-serif !important; }

    .hero h1,
    .hero .recipient,
    .note .note-copy,
    .story-title,
    .reason-title,
    .letter-salutation,
    .surprise-title,
    .seal { font-family: 'Playfair Display', Georgia, serif !important; }

    .topline {
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 3rem;
        border-bottom: 1px solid var(--line);
        color: var(--rose-dark);
        font-size: 0.76rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .wordmark { font-weight: 700; }
    .topline-note { color: var(--muted); letter-spacing: 0.04em; text-transform: none; }

    .hero {
        display: grid;
        grid-template-columns: minmax(0, 1.06fr) minmax(280px, 0.94fr);
        align-items: center;
        gap: clamp(2.5rem, 7vw, 6.5rem);
        min-height: min(690px, 78vh);
        padding: 3.5rem 0 4rem;
    }

    .hero-copy { position: relative; z-index: 1; animation: arrive 850ms ease-out both; }

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 0.65rem;
        margin: 0 0 1.35rem;
        color: var(--rose);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        line-height: 1.5;
        text-transform: uppercase;
    }

    .eyebrow::before {
        width: 1.8rem;
        height: 1px;
        background: currentColor;
        content: "";
    }

    .hero h1 {
        max-width: 13ch;
        margin: 0;
        color: var(--ink);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2.8rem, 5.5vw, 5.15rem);
        font-weight: 500;
        line-height: 1.08;
    }

    .hero-subtitle {
        max-width: 37rem;
        margin: 1.45rem 0 0;
        color: var(--muted);
        font-size: clamp(1rem, 1.35vw, 1.13rem);
        line-height: 1.8;
    }

    .recipient {
        display: inline-block;
        margin-top: 1.55rem;
        color: var(--rose-dark);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.28rem;
        font-style: italic;
    }

    .begin-link {
        display: inline-flex;
        align-items: center;
        gap: 0.8rem;
        min-height: 3.35rem;
        margin-top: 2rem;
        padding: 0.72rem 1.35rem;
        border: 1px solid var(--rose-dark);
        border-radius: 999px;
        background: var(--rose-dark);
        box-shadow: 0 8px 22px rgba(119, 55, 76, 0.15);
        color: #fffaf7 !important;
        font-size: 0.9rem;
        font-weight: 600;
        text-decoration: none !important;
        transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
    }

    .begin-link::after { content: "\\2193"; font-size: 1.05rem; }
    .begin-link:hover { transform: translateY(-2px); background: #642d40; box-shadow: 0 12px 26px rgba(119, 55, 76, 0.23); }
    [data-testid="stMarkdownContainer"] .begin-link:focus-visible {
        outline: 3px solid var(--rose);
        outline-offset: 4px;
    }

    .visual {
        position: relative;
        width: min(100%, 445px);
        justify-self: center;
        animation: arrive 950ms 120ms ease-out both;
    }

    .photo-frame {
        position: relative;
        overflow: hidden;
        aspect-ratio: 0.83;
        border: 8px solid rgba(255, 253, 249, 0.86);
        border-radius: 46% 46% 42% 42% / 38% 38% 34% 34%;
        background: linear-gradient(145deg, var(--blush), var(--lavender));
        box-shadow: 0 24px 70px rgba(93, 56, 65, 0.17), 0 0 0 1px rgba(119, 55, 76, 0.08);
    }

    .photo-frame img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center 52%;
        filter: saturate(0.83) brightness(1.04);
    }

    .photo-wash {
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(255, 250, 244, 0.03) 52%, rgba(69, 42, 51, 0.2));
        pointer-events: none;
    }

    .seal {
        position: absolute;
        right: -1.35rem;
        bottom: 2.4rem;
        display: grid;
        width: 6.5rem;
        aspect-ratio: 1;
        place-items: center;
        border: 1px solid rgba(119, 55, 76, 0.2);
        border-radius: 50%;
        background: rgba(255, 253, 249, 0.9);
        box-shadow: 0 12px 35px rgba(93, 56, 65, 0.13);
        color: var(--rose-dark);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.06rem;
        font-style: italic;
        line-height: 1.2;
        text-align: center;
        transform: rotate(8deg);
    }

    .float-heart {
        position: absolute;
        color: #bd7188;
        filter: drop-shadow(0 0 9px rgba(189, 113, 136, 0.38));
        animation: float 4.8s ease-in-out infinite;
        pointer-events: none;
    }

    .heart-one { top: 6%; right: -4%; font-size: 1.25rem; }
    .heart-two { top: 35%; left: -8%; color: #b5a0bc; font-size: 0.9rem; animation-delay: -1.7s; }
    .heart-three { right: 4%; bottom: 6%; font-size: 0.75rem; animation-delay: -3.1s; }

    .note {
        position: relative;
        display: grid;
        grid-template-columns: auto minmax(0, 1fr);
        align-items: start;
        gap: 1.1rem;
        max-width: 820px;
        margin: 0 auto;
        padding: 2.3rem clamp(1.2rem, 5vw, 3.3rem);
        border-top: 1px solid var(--line);
        border-bottom: 1px solid var(--line);
        scroll-margin-top: 2rem;
    }

    .note-heart {
        display: grid;
        width: 2.65rem;
        aspect-ratio: 1;
        place-items: center;
        border-radius: 50%;
        background: linear-gradient(145deg, #f7e4e5, #eee8f2);
        color: var(--rose-dark);
        font-size: 1.1rem;
    }

    .note-label {
        margin: 0 0 0.5rem;
        color: var(--rose);
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
    }

    .note-copy {
        margin: 0;
        color: var(--ink);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(1.3rem, 2.3vw, 1.8rem);
        line-height: 1.5;
    }

    .footer-note {
        margin: 1.6rem 0 0;
        color: var(--muted);
        font-size: 0.75rem;
        text-align: center;
    }

    .story-section {
        max-width: 980px;
        margin: 1rem auto 0;
        padding: 3.7rem 0 1rem;
        scroll-margin-top: 2rem;
    }

    .section-kicker {
        margin: 0 0 0.7rem;
        color: var(--rose);
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        line-height: 1.6;
        text-transform: uppercase;
    }

    .story-title {
        margin: 0;
        color: var(--ink);
        font-size: clamp(1.9rem, 3.5vw, 2.7rem);
        font-weight: 500;
        line-height: 1.2;
    }

    .section-intro {
        max-width: 38rem;
        margin: 0.8rem 0 0;
        color: var(--muted);
        font-size: 0.98rem;
        line-height: 1.75;
    }

    [data-testid="stColumn"] > [data-testid="stVerticalBlock"]:has(.reason-title) {
        border: 1px solid var(--line) !important;
        border-radius: 8px !important;
        background: rgba(255, 253, 249, 0.72) !important;
        box-shadow: 0 12px 34px rgba(93, 56, 65, 0.06);
        padding: 1rem 1.1rem;
    }

    .reason-index {
        margin: 0 0 0.85rem;
        color: var(--rose);
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
    }

    .reason-title {
        min-height: 2.9em;
        margin: 0;
        color: var(--ink);
        font-size: 1.28rem;
        font-weight: 500;
        line-height: 1.35;
    }

    .reason-copy {
        margin: 0.9rem 0 0;
        padding-top: 0.9rem;
        border-top: 1px solid var(--line);
        color: var(--muted);
        font-size: 0.9rem;
        line-height: 1.7;
        animation: arrive 380ms ease-out both;
    }

    [data-testid="stButton"] > button {
        min-height: 2.9rem;
        border: 1px solid rgba(119, 55, 76, 0.38) !important;
        border-radius: 999px !important;
        background: var(--paper) !important;
        color: var(--rose-dark) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.86rem !important;
        font-weight: 600 !important;
        transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
    }

    [data-testid="stButton"] > button:hover {
        transform: translateY(-1px);
        border-color: var(--rose-dark) !important;
        background: var(--blush) !important;
        box-shadow: 0 6px 16px rgba(119, 55, 76, 0.1);
    }

    [data-testid="stButton"] > button:focus-visible {
        outline: 3px solid var(--rose) !important;
        outline-offset: 3px;
    }

    [data-testid="stButton"] > button[kind="primary"] {
        border-color: var(--rose-dark) !important;
        background: var(--rose-dark) !important;
        color: #fffaf7 !important;
    }

    [data-testid="stButton"] > button[kind="primary"]:hover {
        background: #642d40 !important;
    }

    [data-testid="stExpander"] {
        margin-top: 1.4rem;
        overflow: hidden;
        border: 1px solid var(--line) !important;
        border-radius: 8px !important;
        background: rgba(255, 253, 249, 0.82) !important;
    }

    [data-testid="stExpander"] summary {
        color: var(--rose-dark);
        font-family: 'DM Sans', sans-serif;
        font-weight: 600;
    }

    .letter-paper {
        max-width: 760px;
        margin: 0.4rem auto;
        padding: clamp(1.2rem, 4vw, 2.7rem);
        border-left: 2px solid rgba(168, 79, 104, 0.42);
        background: linear-gradient(110deg, rgba(247, 228, 229, 0.38), rgba(255, 253, 249, 0.35) 60%);
    }

    .letter-salutation {
        margin: 0 0 1.2rem;
        color: var(--rose-dark);
        font-size: 1.38rem;
        font-style: italic;
    }

    .letter-body {
        margin: 0 0 1rem;
        color: var(--ink);
        font-size: 0.98rem;
        line-height: 1.9;
    }

    .letter-signoff {
        margin: 1.5rem 0 0;
        color: var(--rose-dark);
        font-family: 'Playfair Display', Georgia, serif !important;
        font-size: 1.12rem;
        font-style: italic;
        line-height: 1.8;
    }

    .question-reply {
        margin-top: 1.2rem;
        padding: 1rem 1.2rem;
        border-left: 3px solid var(--rose);
        border-radius: 0 8px 8px 0;
        background: linear-gradient(100deg, rgba(247, 228, 229, 0.7), rgba(238, 232, 242, 0.45));
        color: var(--rose-dark);
        font-size: 0.95rem;
        line-height: 1.7;
        animation: arrive 400ms ease-out both;
    }

    .surprise-reveal {
        position: relative;
        overflow: hidden;
        max-width: 760px;
        margin: 1.3rem auto 0;
        padding: clamp(1.6rem, 5vw, 3.5rem);
        border: 1px solid rgba(168, 79, 104, 0.24);
        border-radius: 8px;
        background:
            radial-gradient(ellipse at 92% 8%, rgba(238, 232, 242, 0.85), transparent 48%),
            linear-gradient(135deg, #fffdf9, #f9e9e9 58%, #fffaf4);
        box-shadow: 0 18px 50px rgba(93, 56, 65, 0.11);
        text-align: center;
        animation: reveal 720ms cubic-bezier(0.2, 0.75, 0.25, 1) both;
    }

    .surprise-heart {
        display: inline-grid;
        width: 2.8rem;
        aspect-ratio: 1;
        place-items: center;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.75);
        color: var(--rose);
        font-size: 1.2rem;
        box-shadow: 0 0 24px rgba(168, 79, 104, 0.17);
    }

    .surprise-title {
        margin: 1rem 0 0;
        color: var(--rose-dark);
        font-size: clamp(1.65rem, 4vw, 2.3rem);
        font-weight: 500;
        line-height: 1.25;
    }

    .surprise-copy {
        max-width: 34rem;
        margin: 0.9rem auto 0;
        color: var(--ink);
        font-size: 1rem;
        line-height: 1.8;
    }

    .surprise-signoff {
        margin: 1rem 0 0;
        color: var(--rose-dark);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.1rem;
        font-style: italic;
    }

    @keyframes arrive {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(-8deg); opacity: 0.72; }
        50% { transform: translateY(-10px) rotate(7deg); opacity: 1; }
    }

    @keyframes reveal {
        from { opacity: 0; transform: translateY(16px) scale(0.985); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    @media (max-width: 760px) {
        .block-container { padding: 0.7rem 1.2rem 2rem; }
        .topline { min-height: 2.7rem; font-size: 0.65rem; }
        .topline-note { font-size: 0.72rem; }
        .hero {
            grid-template-columns: minmax(0, 1fr);
            gap: 2.8rem;
            min-height: auto;
            padding: 3.6rem 0 3.1rem;
        }
        .hero-copy { order: 0; }
        .hero h1 { max-width: 12ch; font-size: clamp(2.75rem, 12vw, 4rem); }
        .hero-subtitle { max-width: 32rem; font-size: 1rem; }
        .visual { order: 1; width: min(76%, 340px); }
        .seal { right: -1.2rem; bottom: 1.5rem; width: 5.7rem; font-size: 0.95rem; }
        .heart-two { left: -10%; }
        .note { gap: 0.85rem; padding: 1.8rem 0.2rem; }
        .story-section { padding-top: 2.8rem; }
        [data-testid="stHorizontalBlock"] { flex-direction: column; gap: 0.9rem; }
        [data-testid="stColumn"] { width: 100% !important; min-width: 100% !important; flex: 1 1 100% !important; }
        .reason-title { min-height: 0; }
        [data-testid="stExpander"] { margin-top: 1rem; }
    }

    @media (max-width: 390px) {
        .topline-note { display: none; }
        .visual { width: 82%; }
        .begin-link { min-height: 3.2rem; }
    }

    @media (prefers-reduced-motion: reduce) {
        html { scroll-behavior: auto; }
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_section_heading(section_id, eyebrow, title, intro):
    intro_html = (
        f'<p class="section-intro">{html.escape(intro)}</p>' if intro else ""
    )
    st.markdown(
        f"""
        <section class="story-section" id="{html.escape(section_id)}">
            <p class="section-kicker">{html.escape(eyebrow)}</p>
            <h2 class="story-title">{html.escape(title)}</h2>
            {intro_html}
        </section>
        """,
        unsafe_allow_html=True,
    )


def toggle_reason(reason_index):
    opened_reasons = set(st.session_state["opened_reasons"])
    if reason_index in opened_reasons:
        opened_reasons.remove(reason_index)
    else:
        opened_reasons.add(reason_index)
    st.session_state["opened_reasons"] = sorted(opened_reasons)


def choose_question_reply(option_index):
    st.session_state["question_reply"] = option_index


def reveal_surprise():
    st.session_state["surprise_open"] = True


if "opened_reasons" not in st.session_state:
    st.session_state["opened_reasons"] = []
if "question_reply" not in st.session_state:
    st.session_state["question_reply"] = None
if "surprise_open" not in st.session_state:
    st.session_state["surprise_open"] = False


recipient = html.escape(PERSONAL_CONTENT["recipient"])
headline = html.escape(PERSONAL_CONTENT["headline"])
subtitle = html.escape(PERSONAL_CONTENT["subtitle"])
welcome_note = html.escape(PERSONAL_CONTENT["welcome_note"])

st.markdown(
    f"""
    <div class="topline">
        <span class="wordmark">Project Cupid</span>
                <span class="topline-note">{html.escape(PERSONAL_CONTENT["topline_note"])}</span>
    </div>
    <main>
        <section class="hero" aria-labelledby="welcome-heading">
            <div class="hero-copy">
                <p class="eyebrow">{html.escape(PERSONAL_CONTENT["hero_eyebrow"])}</p>
                <h1 id="welcome-heading">{headline}</h1>
                <p class="hero-subtitle">{subtitle}</p>
                <span class="recipient">For {recipient}</span>
                <div>
                    <a class="begin-link" href="#a-little-note">{html.escape(PERSONAL_CONTENT["begin_button"])}</a>
                </div>
            </div>
            <div class="visual" aria-label="A soft arrangement of flowers">
                <span class="float-heart heart-one" aria-hidden="true">&#9829;</span>
                <span class="float-heart heart-two" aria-hidden="true">&#9829;</span>
                <span class="float-heart heart-three" aria-hidden="true">&#9829;</span>
                <div class="photo-frame">
                    <img
                        src="https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=1100&q=85"
                        alt="Soft pink and white flowers in gentle natural light"
                    >
                    <span class="photo-wash" aria-hidden="true"></span>
                </div>
                <div class="seal" aria-hidden="true">
                    {html.escape(PERSONAL_CONTENT["seal_top"])}<br>
                    {html.escape(PERSONAL_CONTENT["seal_bottom"])}
                </div>
            </div>
        </section>
        <section class="note" id="a-little-note" aria-label="A small welcome note">
            <span class="note-heart" aria-hidden="true">&#9829;</span>
            <div>
                <p class="note-label">{html.escape(PERSONAL_CONTENT["note_label"].format(recipient=PERSONAL_CONTENT["recipient"]))}</p>
                <p class="note-copy">{welcome_note}</p>
            </div>
        </section>
    </main>
    """,
    unsafe_allow_html=True,
)

reasons_section = PERSONAL_CONTENT["reasons_section"]
render_section_heading(
    "reasons", reasons_section["eyebrow"], reasons_section["title"], reasons_section["intro"]
)
reason_columns = st.columns(len(reasons_section["reasons"]))

for reason_index, reason in enumerate(reasons_section["reasons"]):
    with reason_columns[reason_index]:
        with st.container(border=True):
            st.markdown(
                f"""
                <p class="reason-index">{html.escape(reasons_section["reason_label"].format(number=f"{reason_index + 1:02d}"))}</p>
                <h3 class="reason-title">{html.escape(reason["title"])}</h3>
                """,
                unsafe_allow_html=True,
            )
            is_open = reason_index in st.session_state["opened_reasons"]
            st.button(
                reasons_section["close_button"] if is_open else reasons_section["open_button"],
                key=f"reason_{reason_index}",
                on_click=toggle_reason,
                args=(reason_index,),
            )
            if is_open:
                st.markdown(
                    f'<p class="reason-copy">{html.escape(reason["detail"])}</p>',
                    unsafe_allow_html=True,
                )

letter = PERSONAL_CONTENT["letter"]
render_section_heading(
    "letter",
    letter["eyebrow"].format(sender=PERSONAL_CONTENT["sender"]),
    letter["title"],
    letter["intro"],
)

with st.expander(letter["open_button"], expanded=False):
    letter_paragraphs = "".join(
        f'<p class="letter-body">{html.escape(paragraph)}</p>'
        for paragraph in letter["paragraphs"]
    )
    st.markdown(
        f"""
        <article class="letter-paper">
            <p class="letter-salutation">{html.escape(letter["salutation"].format(recipient=PERSONAL_CONTENT["recipient"]))}</p>
            {letter_paragraphs}
            <p class="letter-signoff">
                {html.escape(letter["signoff"])}
            </p>
        </article>
        """,
        unsafe_allow_html=True,
    )

question = PERSONAL_CONTENT["question"]
render_section_heading(
    "question", question["eyebrow"], question["title"], question["intro"]
)
question_columns = st.columns(len(question["options"]))

for option_index, option in enumerate(question["options"]):
    with question_columns[option_index]:
        st.button(
            option["label"],
            key=f"question_option_{option_index}",
            on_click=choose_question_reply,
            args=(option_index,),
            type="primary" if option_index == 0 else "secondary",
        )

selected_reply = st.session_state["question_reply"]
if selected_reply is not None:
    reply = question["options"][selected_reply]["reply"]
    st.markdown(
        f'<div class="question-reply" role="status" aria-live="polite">{html.escape(reply)}</div>',
        unsafe_allow_html=True,
    )

surprise = PERSONAL_CONTENT["surprise"]
render_section_heading(
    "surprise", surprise["eyebrow"], surprise["title"], ""
)
st.button(
    surprise["button"],
    key="open_surprise",
    on_click=reveal_surprise,
    type="primary",
)

if st.session_state["surprise_open"]:
    st.markdown(
        f"""
        <article class="surprise-reveal" role="status" aria-live="polite">
            <span class="surprise-heart" aria-hidden="true">&#9829;</span>
            <h3 class="surprise-title">{html.escape(surprise["revealed_title"])}</h3>
            <p class="surprise-copy">{html.escape(surprise["message"])}</p>
            <p class="surprise-signoff">{html.escape(surprise["signoff"])}</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f'<p class="footer-note">{html.escape(PERSONAL_CONTENT["footer"])}</p>',
    unsafe_allow_html=True,
)