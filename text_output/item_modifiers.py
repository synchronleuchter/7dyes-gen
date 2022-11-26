from text_output import common


prefix = '''<configs>'''

suffix = '''</configs>'''


def body(hsv_color, rgb_color, pigment=False):
    color = f'{rgb_color[0]},{rgb_color[1]},{rgb_color[2]}'
    drop_chance = 'cosmetic_install_chance=".1"' if pigment else ""
    return f'''<append xpath="/item_modifiers">
	<item_modifier name="{common.color_id(rgb_color, pigment)}" installable_tags="clothing,armor,weapon,tool,vehicle,drone" modifier_tags="dye" type="attachment" {drop_chance}>
		<property name="Extends" value="modGeneralMaster"/>
		<property name="DescriptionKey" value="modDyeGroupDesc"/>
		<property name="CustomIcon" value="modDyeWhite"/> <property name="CustomIconTint" value="{color}"/>
		<property name="Material" value="Mpaint"/>
		<property name="Weight" value="20"/>

		<item_property_overrides name="*">
			<property name="TintColor" value="{color}"/>
			<property name="CustomIconTint" value="{color}"/>
			<property name="UMA.Overlay0Tint" value="{color}"/>
		</item_property_overrides>

		<item_property_overrides name="apparelTankTop">
			<property name="UMA.Overlay0Tint" value="skin"/>
			<property name="UMA.Overlay1Tint" value="{color}"/>
		</item_property_overrides>

		<item_property_overrides name="apparelTShirtPlain">
			<property name="UMA.Overlay0Tint" value="skin"/>
			<property name="UMA.Overlay1Tint" value="{color}"/>
		</item_property_overrides>

		<item_property_overrides name="apparelTShirtZU">
			<property name="UMA.Overlay0Tint" value="skin"/>
			<property name="UMA.Overlay1Tint" value="{color}"/>
		</item_property_overrides>

		<item_property_overrides name="apparelCoatJacketLetterZU">
			<property name="UMA.Overlay0Tint" value="{color},255"/>
		</item_property_overrides>

		<item_property_overrides name="apparelDenimShortsPants">
			<property name="UMA.Overlay0Tint" value="skin"/>
			<property name="UMA.Overlay1Tint" value="{color}"/>
		</item_property_overrides>

		<item_property_overrides name="apparelSuitPants">
			<property name="UMA.Overlay0Tint" value="{color}"/>
		</item_property_overrides>

		<item_property_overrides name="apparelSuitJacket">
			<property name="UMA.Overlay0Tint" value="{color}"/>
		</item_property_overrides>
	</item_modifier></append>'''
