from text_output import common

prefix = '''<configs>'''

suffix = '''</configs>'''


def body(i, hsv_cone, rgb_cone, rgb_line, v_steps, colors_per_hue, grayscale, pigment=False):
    if pigment:
        rgb_color = rgb_cone[i]
        color = f'{rgb_color[0]},{rgb_color[1]},{rgb_color[2]}'
        pigment_dust_id = common.pigment_dust_id(rgb_color)
        return f'''<append xpath="/items"><item name="{pigment_dust_id}">
        <property name="HoldType" value="45"/>
        <property name="Meshfile" value="#Other/Items?Misc/sackPrefab.prefab"/>
        <property name="DropMeshfile" value="#Other/Items?Misc/sack_droppedPrefab.prefab"/>
        <property name="Material" value="MresourceCement"/>
        <property name="Weight" value="1"/>
        <property name="NoScrapping" value="true"/>
        <property name="Stacknumber" value="6000"/>
        <property name="EconomicValue" value="0"/>
        <property name="EconomicBundleSize" value="6000"/>
        <property name="Group" value="Resources"/>
        <property name="CustomIcon" value="resourceCement"/>
        <property name="CustomIconTint" value="{color}"/>
    </item></append>'''
    else:
        return ''
