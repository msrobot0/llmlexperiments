import schemdraw
import schemdraw.elements as elm

# Create a new schematic drawing
d = schemdraw.Drawing()

# Define elements
vco = d.add(elm.SourceV().label('VCO', loc='left'))
wave_shaping = d.add(elm.Line().length(2).label('Waveform Shaping\n(Filters, Waveshapers)', loc='left'))
env_generator = d.add(elm.Line().length(2).label('Envelope Generator\n(ADSR, etc.)', loc='left'))
vca = d.add(elm.Line().length(2).label('VCA\n(Voltage-Controlled Amplifier)', loc='left'))

# Output block
output = d.add(elm.Dot())

# Connect elements
d += elm.Line().right().at(vco.end).length(1).tox(wave_shaping.start)
d += elm.Line().right().at(wave_shaping.end).length(1).tox(env_generator.start)
d += elm.Line().right().at(env_generator.end).length(1).tox(vca.start)

# Draw the schematic
d.draw()

# Show the schematic
d.show()
