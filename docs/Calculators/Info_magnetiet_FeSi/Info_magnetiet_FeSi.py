"""
Dense Medium Separation (DMS) - magnetite / FeSi dosing calculator.

"""

import streamlit as st

# streamlit runs this whole file top-to-bottom again on every single
# interaction (every widget change). That's the core mental model: there
# is no persistent "app state" other than what you explicitly keep in
# st.session_state - everything else is just recomputed each run from
# whatever the widgets currently hold.

st.set_page_config(page_title="DMS magnetite / FeSi calculator")

# This app only ever runs inside an <iframe> on the site (see index.md) -
# trim Streamlit's default top padding, which exists to leave room for
# its own header/toolbar, since that space just reads as dead whitespace
# here.
st.markdown(
    "<style>.block-container { padding-top: 1rem; }</style>",
    unsafe_allow_html=True,
)

st.title("Dense medium separation - magnetite / FeSi calculator")

st.markdown(
    "Estimates the amount of magnetite or FeSi (in tons) needed to fill "
    "a dense medium separation (DMS) circuit up to a target medium density."
    "test test test"
)

# The only two materials this calculator is used for, with their typical
# density. Used both to populate the "Material" dropdown and to look up
# the default density for whichever one is selected.
MATERIAL_DENSITIES = {
    "Magnetite": 4.7,
    "FeSi": 6.95,
}

# --- Presets, taken straight from the 3 worksheet tabs -----------------
# Each key is one of the original Excel sheet names. "Custom" isn't from
# the sheet; it's just the option that leaves every field at 0 so you
# can fill in a DMS unit that isn't one of these 3. Material density
# isn't listed here anymore - it's always looked up from
# MATERIAL_DENSITIES based on whichever material is selected below.

PRESETS = {
    "Custom": {
        "material": "Magnetite",
        "target_density": 1.0,
        "overflow": 0.0,
        "drum_content": 0.0,
        "tank": 0.0,
        "pipes": 0.0,
    },
    "DMS 1.4": {
        "material": "Magnetite",
        "target_density": 1.4,
        "overflow": 0.0,
        "drum_content": 0.0,
        "tank": 0.0,
        "pipes": 0.0,
    },
    "DMS 2.2": {
        "material": "FeSi",
        "target_density": 2.2,
        "overflow": 0.0,
        "drum_content": 0.0,
        "tank": 0.0,
        "pipes": 0.0,
    },
    "DMS 3.2": {
        "material": "FeSi",
        "target_density": 3.2,
        "overflow": 0.0,
        "drum_content": 0.0,
        "tank": 0.0,
        "pipes": 0.0,
    },
}

preset_name = st.selectbox("Preset", options=list(PRESETS.keys()), index=0)
preset = PRESETS[preset_name]

# Every widget below gets key=f"..._{preset_name}". That's the trick that
# makes "prefill but stay editable" work: Streamlit treats a widget with
# a new key as a brand-new widget, so switching the preset resets the
# fields to that preset's numbers. Typing into a field only overrides it
# for as long as you stay on that same preset - flip to another preset
# and back, and your edit is gone (it's a fresh widget again). If you
# instead want edits to survive a preset switch, this would need
# st.session_state managed by hand rather than the key= shortcut.

st.subheader("Material")

col1, col2 = st.columns(2)
with col1:
    material_options = list(MATERIAL_DENSITIES.keys())
    material = st.selectbox(
        "Material",
        options=material_options,
        index=material_options.index(preset["material"]),
        key=f"material_{preset_name}",
    )
with col2:
    # This field's key includes `material`, not just `preset_name` - so
    # switching Magnetite <-> FeSi also resets it to that material's
    # typical density (a fresh widget, new default), the same trick used
    # for the preset switch above. It stays editable afterwards in case
    # the real density on site differs from the typical value.
    material_density = st.number_input(
        "Material density (t/m³)",
        min_value=0.0,
        value=MATERIAL_DENSITIES[material],
        step=0.05,
        key=f"material_density_{preset_name}_{material}",
    )

target_density = st.number_input(
    "Target medium density (t/m³)",
    min_value=0.0,
    value=preset["target_density"],
    step=0.05,
    key=f"target_density_{preset_name}",
)

st.subheader("Circuit volumes (m³)")

col3, col4 = st.columns(2)
with col3:
    overflow = st.number_input(
        "Mediumdrum theoretical overflow",
        min_value=0.0,
        value=preset["overflow"],
        step=0.1,
        key=f"overflow_{preset_name}",
    )
    tank = st.number_input(
        "Mediumtank (1.5 m working level)",
        min_value=0.0,
        value=preset["tank"],
        step=0.1,
        key=f"tank_{preset_name}",
    )
with col4:
    drum_content = st.number_input(
        "Mediumdrum theoretical content",
        min_value=0.0,
        value=preset["drum_content"],
        step=0.1,
        key=f"drum_content_{preset_name}",
    )
    pipes = st.number_input(
        "Pipes medium circuit",
        min_value=0.0,
        value=preset["pipes"],
        step=0.1,
        key=f"pipes_{preset_name}",
    )

total_volume = overflow + drum_content + tank + pipes

st.divider()

# material_density == 1 would divide by zero below (it's the density of
# water, which cancels out the whole mix-ratio formula) - guard it
# instead of letting Streamlit crash the page.
if material_density <= 1:
    st.error(
        "Material density must be greater than 1 t/m³ "
        "(it has to be denser than water for this formula to work)."
    )
else:
    # Volume fraction of solids needed to raise a water-based suspension
    # from density 1 (pure water) up to target_density, given solids of
    # material_density: (target_density - 1) / (material_density - 1).
    # Multiplying by material_density converts that volume fraction into
    # a mass of solids per m3 of medium. The final *1.25 is a 25% margin
    # from the original spreadsheet (covers medium losses / makeup).
    mix_ratio = (target_density - 1) / (material_density - 1)
    total_needed = total_volume * mix_ratio * material_density * 1.25

    col5, col6 = st.columns(2)
    col5.metric("Total volume", f"{total_volume:.2f} m³")
    col6.metric(f"{material} needed", f"{total_needed:.2f} tons")