import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_chrono",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    print(build_dir)
    _component_func = components.declare_component("streamlit_chrono", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def chrono(
    items: list,
    active_item_index: int = 0,
    allow_dynamic_update: bool = True,
    borderless_cards: bool = True,
    card_height: int = 200,
    card_less: bool = True,
    card_position_horizontal: str = "BOTTOM",
    card_width: int = 400,
    disable_autoscroll_on_click: bool = True,
    disable_click_on_circle: bool = True,
    disable_nav_on_key: bool = True,
    enable_outline: bool = False,
    flip_layout: bool = False,
    hide_controls=True,
    item_width: int = None,
    line_width: int = 5,
    mode: str = "HORIZONTAL",
    scrollable: bool = False,
    show_all_cards_horizontal: bool = False,
    slide_item_duration: int = 10,
    slide_show: bool = False,
    chrono_theme: dict = None,
    timeline_circle_dimension: int = 15,
    use_read_more: bool = False,
    font_sizes: dict = None,
    button_texts: dict = None,
    timeline_point_shape: str = "circle",
    timeline_point_dimension: int = 15,
    key=None,
):
    """Create a new instance of "chrono".

    Parameters
    ----------
    items: list
        A list of dictionaries describing each item in the timeline

    active_item_index: int
        Active item in the timeline

    allow_dynamic_update: bool
        This property allows timeline items to be updated dynamically.

    borderless_cards: bool
        By enabling this property, the border and shadow on the timeline cards can be removed

    card_height: int
        This property sets the minimum height of the timeline card.

    card_less: bool
        This property disables the display of timeline cards in both horizontal and vertical modes.

    card_position_horizontal: str
        This property positions the timeline card in horizontal mode. The value can be either TOP or BOTTOM.

    card_width: int
        This property sets the maximum width of the timeline card.

    disable_autoscroll_on_click: bool
        This property disables the timeline from auto-scrolling when a timeline card is clicked.

    disable_click_on_circle: bool
        This property disables click action on the circular points.

    disable_nav_on_key: bool
        This property disables keyboard navigation.

    enable_outline: bool
        Enabling this property displays the outline menu on VERTICAL and VERTICAL_ALTERNATING modes.

    flip_layout: bool
        This property flips the layout to right-to-left (RTL).

    hide_controls: bool
        Enabling this property hides the navigation controls.

    item_width: int
        This property sets the width of the timeline section in HORIZONTAL mode.

    line_width: int
        This property is used to customize the width of the timeline track line.

    mode: str
        This property sets the mode of the timeline component. The value can be HORIZONTAL, VERTICAL, or VERTICAL_ALTERNATING.

    scrollable: bool
        This property makes the timeline scrollable in VERTICAL and VERTICAL_ALTERNATING modes.

    show_all_cards_horizontal: bool
        Enabling this property in horizontal mode displays all the cards instead of only the active one.

    slide_item_duration: int
        This property sets the duration (in ms) for which the timeline card is active during a slideshow.

    slide_show: bool
        Enabling this property displays the slideshow control.

    chrono_theme: dict
        This property is used to customize the colors of the timeline component. Renamed from theme because
        streamlit automatically passes its own theme dictionary via props.

    timeline_circle_dimension: int
        This property sets the dimensions of the circular points on the timeline.

    use_read_more: bool
        Enabling this property displays the "read more" button, which is only available if the text content on the card is taller than the card itself.

    font_sizes: dict
        This property is used to customize the font sizes.

    button_texts: dict
        This property is used to customize the alt text for all buttons.

    timeline_point_shape: str
        Shape of each timeline point (square, circle etc.)

    timeline_point_dimension: int
        Specifies the dimensions of the timeline points in pixels

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    current_item: dict
        Selected item from the onSelectItem callback

    """

    current_item = _component_func(
        items=items,
        active_item_index=active_item_index,
        allow_dynamic_update=allow_dynamic_update,
        borderless_cards=borderless_cards,
        card_height=card_height,
        card_less=card_less,
        card_position_horizontal=card_position_horizontal,
        card_width=card_width,
        disable_autoscroll_on_click=disable_autoscroll_on_click,
        disable_click_on_circle=disable_click_on_circle,
        disable_nav_on_key=disable_nav_on_key,
        enable_outline=enable_outline,
        flip_layout=flip_layout,
        hide_controls=hide_controls,
        item_width=item_width,
        line_width=line_width,
        mode=mode,
        scrollable=scrollable,
        show_all_cards_horizontal=show_all_cards_horizontal,
        slide_item_duration=slide_item_duration,
        slide_show=slide_show,
        chrono_theme=chrono_theme,
        timeline_circle_dimension=timeline_circle_dimension,
        use_read_more=use_read_more,
        font_sizes=font_sizes,
        button_texts=button_texts,
        timeline_point_dimension=timeline_point_dimension,
        timeline_point_shape=timeline_point_shape,
        key=key,
    )

    return current_item


# Testing Ground
if not _RELEASE:
    import streamlit as st

    st.subheader("Component with constant args")

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    items = [
        {
            "title": "May 2023",
            "cardTitle": "Event 1",
            "cardSubtitle": "Event 1 Subtitle",
            "cardDetailedText": "This is the first event on the timeline.",
        },
        {
            "title": "June 2023",
            "cardTitle": "Event 2",
            "cardSubtitle": "Event 2 Subtitle",
            "cardDetailedText": "This is the second event on the timeline.",
        },
        {
            "title": "July 2023",
            "cardTitle": "Event 3",
            "cardSubtitle": "Event 3 Subtitle",
            "cardDetailedText": "This is the third event on the timeline.",
        },
    ]
    chrono_theme={
        "secondary": "#7a0fe6",
        "primary": "#f1e6fc",
        "titleColorActive": "white",
        "titleColor": "black"
    }
    current_item = chrono(items,
                          active_item_index=0,
                          chrono_theme=chrono_theme,
                          timeline_circle_dimension=0,
                          timeline_point_dimension=20,
                          item_width=150,
                          key="foo")
    print(current_item)
