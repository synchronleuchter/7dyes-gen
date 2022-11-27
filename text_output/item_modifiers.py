from text_output import common
import colors

prefix = '''<configs>'''

suffix = '''</configs>'''


def body(i, hsv_cone, rgb_cone, rgb_line, v_steps, colors_per_hue, grayscale, pigment=False):
    rgb_color = rgb_cone[i] if not grayscale else rgb_line[i]
    color = f'{rgb_color[0]},{rgb_color[1]},{rgb_color[2]}'
    corresponding_pigment = rgb_cone[colors.corresponding_pigment_index(i, colors_per_hue)]
    pigment_dust_id = common.pigment_dust_id(corresponding_pigment)
    drop_chance = 'cosmetic_install_chance=".1"' if pigment else ''
    open_action = f'''<property class="Action0">
			<property name="Class" value="OpenBundle"/>
			<property name="Create_item" value="{pigment_dust_id}"/>
			<property name="Create_item_count" value="1"/>
		</property>''' if not grayscale else ''
    return f'''<append xpath="/item_modifiers">
	<item_modifier name="{common.color_id(rgb_color, pigment)}" installable_tags="clothing,armor,weapon,tool,vehicle,drone" modifier_tags="dye" type="attachment" {drop_chance}>
		<property name="Extends" value="modGeneralMaster"/>
		<property name="DescriptionKey" value="modDyeGroupDesc"/>
		<property name="CustomIcon" value="modDyeWhite"/> <property name="CustomIconTint" value="{color}"/>
		<property name="Material" value="Mpaint"/>
		<property name="Weight" value="20"/>
		{open_action}
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
