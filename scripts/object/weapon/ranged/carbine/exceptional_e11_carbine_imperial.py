import sys

def setup(core, object)::
	object.setStringAttribute('required_skill', 'None')
	object.setStringAttribute('faction_restriction', 'Imperial')
	object.setAttackSpeed(0.6);
	object.setCustomName('Exceptional Imperial E-11 Carbine');
	object.setMaxRange(50);
	object.setDamageType("energy");
	object.setMinDamage(310);
	object.setMaxDamage(550);
	object.setWeaponType(1);
	return