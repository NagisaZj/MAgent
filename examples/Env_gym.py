import magent

class gym_env():
    def __init__(self):
        return

    def reset_world(self,map_name,map_size,num_walls,num_predators,num_preys,algorithm,render_dir = './build/render'):
        self.env = magent.GridWorld(map_name, map_size=map_size)
        self.env.set_render_dir(render_dir)

        # get group handles
        self.predator, self.prey = self.env.get_handles()
        self.alg = algorithm
        # init env and agents
        self.env.reset()
        self.env.add_walls(method="random", n=num_walls)
        self.env.add_agents(self.predator, method="random", n=num_predators)
        self.env.add_agents(self.prey, method="random", n=num_preys)
        self.get_observation()



    def get_observation(self):
        obs_1 = self.env.get_observation(self.predator)
        ids_1 = self.env.get_agent_id(self.predator)
        obs_2 = self.env.get_observation(self.prey)
        ids_2 = self.env.get_agent_id(self.prey)
        print([obs.shape for obs in obs_1])
        print(ids_1.shape)
        if self.alg =='MF':
            return obs_1,ids_1,obs_2,ids_2
        else:
            return


if __name__ == '__main__':
    env = gym_env()
    env.reset_world('pursuit',15,1,2,2)
