from pydantic import BaseModel, Field

class GAParams(BaseModel):
    """
    Class to hold the parameters used for the genetic algorithm.
    """

    num_parents: int = Field(
        default=10,
        description="Number of parent members to retain in each generation."
    )
    num_kids: int = Field(
        default=10,
        description="Number of children to produce from the parent members."
    )
    num_generations: int = Field(
        default=500,
        description="Total number of generations to simulate in the genetic algorithm."
    )
    num_members: int = Field(
        default=200,
        description="Total number of members in each generation of the population."
    )
    tolerance: float = Field(
        default=0.5,
        description="This parameter sets the threshold for considering the deviation of "
                    "concentration factors from their ideal values. It is used to adjust "
                    "the sensitivity of the cost function to variations in material "
                    "property concentrations, with a lower tolerance indicating "
                    "stricter requirements for concentration matching. In the cost "
                    "function, tolerance helps to determine the weight applied to "
                    "concentration factors, influencing the penalty for deviations in "
                    "material properties from their desired values."
    )
    weight_eff_prop: float = Field(
        default=10.0,
        description="This weight factor scales the importance of the effective property "
                    "matching component of the cost function. It determines how "
                    "strongly the difference between the calculated effective "
                    "properties of the composite material and the desired properties "
                    "influences the total cost. A higher value places more emphasis "
                    "on accurately matching these effective properties, aiming to "
                    "optimize the material composition towards achieving specific "
                    "property targets."
    )
    weight_conc_factor: float = Field(
        default=0.5,
        description="This weight factor controls the significance of the "
                    "concentration factor matching in the cost function. It scales "
                    "the penalty applied for deviations of concentration factors "
                    "from their ideal or tolerated levels, thus affecting the "
                    "optimization process's focus on material distribution within "
                    "the composite. A higher value means that achieving the "
                    "desired concentration balance between the composite's "
                    "constituents is more critical to minimizing the overall cost."
    )

    #------ Getter Methods ------#
    def get_num_parents(self):
        return self.num_parents
    
    def get_num_kids(self):
        return self.num_kids
    
    def get_num_generations(self):
        return self.num_generations
    
    def get_num_members(self):
        return self.num_members
    
    def get_tolerance(self):
        return self.tolerance
    
    def get_weight_eff_prop(self):
        return self.weight_eff_prop
    
    def get_weight_conc_factor(self):
        return self.weight_conc_factor
    
    #------ Setter Methods ------#
    def set_num_parents(self, num_parents):
        self.num_parents = num_parents
        return self
    
    def set_num_kids(self, num_kids):
        self.num_kids = num_kids
        return self
    
    def set_num_generations(self, num_generations):
        self.num_generations = num_generations
        return self
    
    def set_num_members(self, num_members):
        self.num_members = num_members
        return self
    
    def set_tolerance(self, tolerance):
        self.tolerance = tolerance
        return self
    
    def set_weight_eff_prop(self, weight_eff_prop):
        self.weight_eff_prop = weight_eff_prop
        return self
    
    def set_weight_conc_factor(self, weight_conc_factor):
        self.weight_conc_factor = weight_conc_factor
        return self

    

