from typing import Union

from main.api_client.schemas.pattern_item_category import PatternItemCategory
from main.api_client.schemas.pattern_item_information_schema import PatternItemInformationSchema
from main.api_client.schemas.pattern_item_list_selector_schema import PatternItemListSelectorSchema
from main.api_client.schemas.pattern_item_numeric_value_schema import PatternItemNumericValueSchema
from main.api_client.schemas.pattern_item_section import PatternItemSection
from main.api_client.schemas.pattern_item_slider_schema import PatternItemSliderSchema
from main.api_client.schemas.pattern_item_text_comment_schema import PatternItemTextCommentSchema
from main.api_client.schemas.pattern_item_yes_no_schema import PatternItemYesNoSchema

PatternItem = Union[
    PatternItemSection,
    PatternItemCategory,
    PatternItemYesNoSchema,
    PatternItemSliderSchema,
    PatternItemListSelectorSchema,
    PatternItemNumericValueSchema,
    PatternItemTextCommentSchema,
    PatternItemInformationSchema
]