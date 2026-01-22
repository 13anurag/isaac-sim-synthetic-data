import omni.replicator.core as rep
with rep.new_layer():
# Add Default Light
distance_light = rep.create.light(rotation=(315,0,0), intensity=3000,
light_type="distant")
sphere = rep.create.sphere(semantics=[('class', 'sphere')], position=(0, 100, 100))
cube = rep.create.cube(semantics= [('class', 'cube')], position=(200, 200 , 100) )
plane = rep.create.plane(scale=10, visible=True)
def sphere_lights(num):
lights = rep.create.light(
light_type="Sphere",
temperature=rep.distribution.normal(6500, 500),
intensity=rep.distribution.normal(35000, 5000),
position=rep.distribution.uniform((-300, -300, -300), (300, 300, 300)),
scale=rep.distribution.uniform(50, 100),
count=num
)
return lights.node
rep.randomizer.register(sphere_lights)
with rep.trigger.on_frame(num_frames=10):
rep.randomizer.sphere_lights(10)