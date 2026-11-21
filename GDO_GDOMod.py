from gdo.base.GDO import GDO
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_Decimal import GDT_Decimal
from gdo.core.GDT_String import GDT_String
from gdo.core.GDT_Unique import GDT_Unique


class GDO_GDOMod(GDO):
    """A catalog entry, not an entitlement or a purchase."""

    def gdo_cached(self):
        return False

    def gdo_columns(self):
        return [
            GDT_AutoInc('gdomod_id'),
            GDT_String('gdomod_framework').ascii().maxlen(16).not_null(),
            GDT_String('gdomod_name').ascii().maxlen(96).not_null(),
            GDT_Decimal('gdomod_monthly_price').digits(11, 2).min(0),
            GDT_Decimal('gdomod_yearly_price').digits(11, 2).min(0),
            GDT_Decimal('gdomod_lifetime_price').digits(11, 2).min(0),
            GDT_Bool('gdomod_prices_placeholder').not_null().initial('1'),
            GDT_Unique('unique_gdomod_framework_name').unique_columns('gdomod_framework', 'gdomod_name'),
        ]
