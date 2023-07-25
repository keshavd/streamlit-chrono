import React, {ReactNode} from "react";
import {Streamlit, StreamlitComponentBase, withStreamlitConnection} from "streamlit-component-lib";
import { Chrono } from 'react-chrono';

class StreamlitChrono extends StreamlitComponentBase{
    public state = {currentItem: {}}
    render = (): ReactNode => {
        const items = this.props.args["items"]
        const activeItemIndex = this.props.args["active_item_index"]
        const allowDynamicUpdate = this.props.args["allow_dynamic_update"]
        const borderlessCards = this.props.args["borderless_cards"]
        const cardHeight = this.props.args["card_height"]
        const cardLess = this.props.args["card_less"]
        const cardPositionHorizontal = this.props.args["card_position_horizontal"]
        const cardWidth = this.props.args["card_width"]
        const disableAutoScrollOnClick = this.props.args["disable_autoscroll_on_click"]
        const disableClickOnCircle = this.props.args["disable_click_on_circle"]
        const disableNavOnKey = this.props.args["disable_nav_on_key"]
        const enableOutline = this.props.args["enable_outline"]
        const flipLayout = this.props.args["flip_layout"]
        const hideControls = this.props.args["hide_controls"]
        const itemWidth =  this.props.args["item_width"]
        const lineWidth = this.props.args["line_width"]
        const mode = this.props.args["mode"]
        const scrollable= this.props.args["scrollable"]
        const showAllCardsHorizontal = this.props.args["show_all_cards_horizontal"]
        const slideItemDuration = this.props.args["slide_item_duration"]
        const slideShow = this.props.args["slide_show"]
        const chronoTheme = this.props.args["chrono_theme"]
        const timelineCircleDimension = this.props.args["timeline_circle_dimension"]
        const useReadMore = this.props.args["use_read_more"]
        const fontSizes = this.props.args["font_sizes"]
        const buttonTexts = this.props.args["button_texts"]
        const timelinePointShape = this.props.args["timeline_point_shape"]
        const timelinePointDimension = this.props.args["timeline_point_dimension"]
        const {theme} = this.props
        return(
            <Chrono
                items={items}
                activeItemIndex={activeItemIndex}
                allowDynamicUpdate={allowDynamicUpdate}
                borderlessCards={borderlessCards}
                cardHeight={cardHeight}
                cardLess={cardLess}
                cardPositionHorizontal={cardPositionHorizontal}
                cardWidth={cardWidth}
                disableAutoScrollOnClick={disableAutoScrollOnClick}
                disableClickOnCircle={disableClickOnCircle}
                disableNavOnKey={disableNavOnKey}
                enableOutline={enableOutline}
                flipLayout={flipLayout}
                hideControls={hideControls}
                itemWidth={itemWidth}
                lineWidth={lineWidth}
                mode={"HORIZONTAL"}
                scrollable={scrollable}
                showAllCardsHorizontal={showAllCardsHorizontal}
                slideItemDuratio={slideItemDuration}
                slideShow={slideShow}
                timelinePointShape={timelinePointShape}
                timelineCircleDimension={timelineCircleDimension}
                useReadMore={useReadMore}
                fontSizes={fontSizes ? fontSizes : null}
                buttonTexts={buttonTexts ? buttonTexts: null}
                timelinePointDimension={timelinePointDimension}
                theme={ chronoTheme ? chronoTheme :
                    {
                        'primary': theme?.primaryColor,
                        'secondary': theme?.secondaryBackgroundColor,
                        'titleColor': theme?.textColor,
                        'titleColorActive': theme?.secondaryBackgroundColor
                    }
                }
                onItemSelected={this.onItemSelected}
            />
        )
    }
    private onItemSelected = (selectedItem: object): void => {
        this.setState(
            prevState => ({currentItem: selectedItem}), () => Streamlit.setComponentValue(this.state.currentItem)
        )
    }
}
export default withStreamlitConnection(StreamlitChrono)
