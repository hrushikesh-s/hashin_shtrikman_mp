class UserInput:

    def __init__(
        self,
        include_carrier_transport:                        bool  = True,
        include_dielectric:                               bool  = True,
        include_elastic:                                  bool  = True,
        include_magnetic:                                 bool  = True,
        include_piezoelectric:                            bool  = True,
        desired_elec_cond_300k_low_doping:                float = 1e-5,
        desired_therm_cond_300k_low_doping:               float = 1e-5,
        desired_e_total:                                  float = 1e-5,
        desired_e_ionic:                                  float = 1e-5,
        desired_e_electronic:                             float = 1e-5,
        desired_n:                                        float = 1e-5,
        desired_bulk_modulus:                             float = 1e-5,
        desired_shear_modulus:                            float = 1e-5,
        desired_universal_anisotropy:                     float = 1e-5,
        desired_total_magnetization:                      float = 1e-5,
        desired_total_magnetization_normalized_volume:    float = 1e-5,
        desired_e_ij:                                     float = 1e-5,
        mat1_lower_elec_cond_300k_low_doping:             float = 1e-5,
        mat1_lower_therm_cond_300k_low_doping:            float = 1e-5,
        mat1_lower_e_total:                               float = 1e-5,
        mat1_lower_e_ionic:                               float = 1e-5,
        mat1_lower_e_electronic:                          float = 1e-5,
        mat1_lower_n:                                     float = 1e-5,
        mat1_lower_bulk_modulus:                          float = 1e-5,
        mat1_lower_shear_modulus:                         float = 1e-5,
        mat1_lower_universal_anisotropy:                  float = 1e-5,
        mat1_lower_total_magnetization:                   float = 1e-5,
        mat1_lower_total_magnetization_normalized_volume: float = 1e-5,
        mat1_lower_e_ij:                                  float = 1e-5,
        mat1_upper_elec_cond_300k_low_doping:             float = 1e-5,
        mat1_upper_therm_cond_300k_low_doping:            float = 1e-5,
        mat1_upper_e_total:                               float = 1e-5,
        mat1_upper_e_ionic:                               float = 1e-5,
        mat1_upper_e_electronic:                          float = 1e-5,
        mat1_upper_n:                                     float = 1e-5,
        mat1_upper_bulk_modulus:                          float = 1e-5,
        mat1_upper_shear_modulus:                         float = 1e-5,
        mat1_upper_universal_anisotropy:                  float = 1e-5,
        mat1_upper_total_magnetization:                   float = 1e-5,
        mat1_upper_total_magnetization_normalized_volume: float = 1e-5,
        mat1_upper_e_ij:                                  float = 1e-5,
        mat2_lower_elec_cond_300k_low_doping:             float = 1e-5,
        mat2_lower_therm_cond_300k_low_doping:            float = 1e-5,
        mat2_lower_e_total:                               float = 1e-5,
        mat2_lower_e_ionic:                               float = 1e-5,
        mat2_lower_e_electronic:                          float = 1e-5,
        mat2_lower_n:                                     float = 1e-5,
        mat2_lower_bulk_modulus:                          float = 1e-5,
        mat2_lower_shear_modulus:                         float = 1e-5,
        mat2_lower_universal_anisotropy:                  float = 1e-5,
        mat2_lower_total_magnetization:                   float = 1e-5,
        mat2_lower_total_magnetization_normalized_volume: float = 1e-5,
        mat2_lower_e_ij:                                  float = 1e-5,
        mat2_upper_elec_cond_300k_low_doping:             float = 1e-5,
        mat2_upper_therm_cond_300k_low_doping:            float = 1e-5,
        mat2_upper_e_total:                               float = 1e-5,
        mat2_upper_e_ionic:                               float = 1e-5,
        mat2_upper_e_electronic:                          float = 1e-5,
        mat2_upper_n:                                     float = 1e-5,
        mat2_upper_bulk_modulus:                          float = 1e-5,
        mat2_upper_shear_modulus:                         float = 1e-5,
        mat2_upper_universal_anisotropy:                  float = 1e-5,
        mat2_upper_total_magnetization:                   float = 1e-5,
        mat2_upper_total_magnetization_normalized_volume: float = 1e-5,
        mat2_upper_e_ij:                                  float = 1e-5
        ):
        self.include_carrier_transport                        = include_carrier_transport
        self.include_dielectric                               = include_dielectric       
        self.include_elastic                                  = include_elastic
        self.include_magnetic                                 = include_magnetic
        self.include_piezoelectric                            = include_piezoelectric
        self.desired_elec_cond_300k_low_doping                = desired_elec_cond_300k_low_doping
        self.desired_therm_cond_300k_low_doping               = desired_therm_cond_300k_low_doping
        self.desired_e_total                                  = desired_e_total
        self.desired_e_ionic                                  = desired_e_ionic
        self.desired_e_electronic                             = desired_e_electronic
        self.desired_n                                        = desired_n
        self.desired_bulk_modulus                             = desired_bulk_modulus
        self.desired_shear_modulus                            = desired_shear_modulus
        self.desired_universal_anisotropy                     = desired_universal_anisotropy
        self.desired_total_magnetization                      = desired_total_magnetization
        self.desired_total_magnetization_normalized_volume    = desired_total_magnetization_normalized_volume
        self.desired_e_ij                                     = desired_e_ij
        self.mat1_lower_elec_cond_300k_low_doping             = mat1_lower_elec_cond_300k_low_doping
        self.mat1_lower_therm_cond_300k_low_doping            = mat1_lower_therm_cond_300k_low_doping
        self.mat1_lower_e_total                               = mat1_lower_e_total
        self.mat1_lower_e_ionic                               = mat1_lower_e_ionic
        self.mat1_lower_e_electronic                          = mat1_lower_e_electronic
        self.mat1_lower_n                                     = mat1_lower_n
        self.mat1_lower_bulk_modulus                          = mat1_lower_bulk_modulus
        self.mat1_lower_shear_modulus                         = mat1_lower_shear_modulus
        self.mat1_lower_universal_anisotropy                  = mat1_lower_universal_anisotropy
        self.mat1_lower_total_magnetization                   = mat1_lower_total_magnetization
        self.mat1_lower_total_magnetization_normalized_volume = mat1_lower_total_magnetization_normalized_volume
        self.mat1_lower_e_ij                                  = mat1_lower_e_ij
        self.mat1_upper_elec_cond_300k_low_doping             = mat1_upper_elec_cond_300k_low_doping
        self.mat1_upper_therm_cond_300k_low_doping            = mat1_upper_therm_cond_300k_low_doping
        self.mat1_upper_e_total                               = mat1_upper_e_total
        self.mat1_upper_e_ionic                               = mat1_upper_e_ionic
        self.mat1_upper_e_electronic                          = mat1_upper_e_electronic
        self.mat1_upper_n                                     = mat1_upper_n
        self.mat1_upper_bulk_modulus                          = mat1_upper_bulk_modulus
        self.mat1_upper_shear_modulus                         = mat1_upper_shear_modulus
        self.mat1_upper_universal_anisotropy                  = mat1_upper_universal_anisotropy
        self.mat1_upper_total_magnetization                   = mat1_upper_total_magnetization
        self.mat1_upper_total_magnetization_normalized_volume = mat1_upper_total_magnetization_normalized_volume
        self.mat1_upper_e_ij                                  = mat1_upper_e_ij   
        self.mat2_lower_elec_cond_300k_low_doping             = mat2_lower_elec_cond_300k_low_doping
        self.mat2_lower_therm_cond_300k_low_doping            = mat2_lower_therm_cond_300k_low_doping
        self.mat2_lower_e_total                               = mat2_lower_e_total
        self.mat2_lower_e_ionic                               = mat2_lower_e_ionic
        self.mat2_lower_e_electronic                          = mat2_lower_e_electronic
        self.mat2_lower_n                                     = mat2_lower_n
        self.mat2_lower_bulk_modulus                          = mat2_lower_bulk_modulus
        self.mat2_lower_shear_modulus                         = mat2_lower_shear_modulus
        self.mat2_lower_universal_anisotropy                  = mat2_lower_universal_anisotropy
        self.mat2_lower_total_magnetization                   = mat2_lower_total_magnetization
        self.mat2_lower_total_magnetization_normalized_volume = mat2_lower_total_magnetization_normalized_volume
        self.mat2_lower_e_ij                                  = mat2_lower_e_ij
        self.mat2_upper_elec_cond_300k_low_doping             = mat2_upper_elec_cond_300k_low_doping
        self.mat2_upper_therm_cond_300k_low_doping            = mat2_upper_therm_cond_300k_low_doping
        self.mat2_upper_e_total                               = mat2_upper_e_total
        self.mat2_upper_e_ionic                               = mat2_upper_e_ionic
        self.mat2_upper_e_electronic                          = mat2_upper_e_electronic
        self.mat2_upper_n                                     = mat2_upper_n
        self.mat2_upper_bulk_modulus                          = mat2_upper_bulk_modulus
        self.mat2_upper_shear_modulus                         = mat2_upper_shear_modulus
        self.mat2_upper_universal_anisotropy                  = mat2_upper_universal_anisotropy
        self.mat2_upper_total_magnetization                   = mat2_upper_total_magnetization
        self.mat2_upper_total_magnetization_normalized_volume = mat2_upper_total_magnetization_normalized_volume
        self.mat2_upper_e_ij                                  = mat2_upper_e_ij     

    
DEFAULT_USER_INPUT = UserInput(include_carrier_transport                         = True,
                                include_dielectric                               = True,
                                include_elastic                                  = True,
                                include_magnetic                                 = True,
                                include_piezoelectric                            = True,
                                desired_elec_cond_300k_low_doping                = 3e5,
                                desired_therm_cond_300k_low_doping               = 15e1,
                                desired_e_total                                  = 5e1,
                                desired_e_ionic                                  = 5e1,
                                desired_e_electronic                             = 5e1,
                                desired_n                                        = 5e1,
                                desired_bulk_modulus                             = 1e2,
                                desired_shear_modulus                            = 1e2,
                                desired_universal_anisotropy                     = 5e1,
                                desired_total_magnetization                      = 5e1,
                                desired_total_magnetization_normalized_volume    = 5e1,
                                desired_e_ij                                     = 5e1,
                                mat1_lower_elec_cond_300k_low_doping             = 0,
                                mat1_lower_therm_cond_300k_low_doping            = 0,
                                mat1_lower_e_total                               = 0,
                                mat1_lower_e_ionic                               = 0,
                                mat1_lower_e_electronic                          = 0,
                                mat1_lower_n                                     = 0,
                                mat1_lower_bulk_modulus                          = 0,
                                mat1_lower_shear_modulus                         = 0,
                                mat1_lower_universal_anisotropy                  = 0,
                                mat1_lower_total_magnetization                   = 0,
                                mat1_lower_total_magnetization_normalized_volume = 0,
                                mat1_lower_e_ij                                  = 0,
                                mat1_upper_elec_cond_300k_low_doping             = 1e9,
                                mat1_upper_therm_cond_300k_low_doping            = 1e9,
                                mat1_upper_e_total                               = 1e9,
                                mat1_upper_e_ionic                               = 1e9,
                                mat1_upper_e_electronic                          = 1e9,
                                mat1_upper_n                                     = 1e9,
                                mat1_upper_bulk_modulus                          = 1e9,
                                mat1_upper_shear_modulus                         = 1e9,
                                mat1_upper_universal_anisotropy                  = 1e9,
                                mat1_upper_total_magnetization                   = 1e9,
                                mat1_upper_total_magnetization_normalized_volume = 1e9,
                                mat1_upper_e_ij                                  = 1e9,
                                mat2_lower_elec_cond_300k_low_doping             = 0,
                                mat2_lower_therm_cond_300k_low_doping            = 0,
                                mat2_lower_e_total                               = 0,
                                mat2_lower_e_ionic                               = 0,
                                mat2_lower_e_electronic                          = 0,
                                mat2_lower_n                                     = 0,
                                mat2_lower_bulk_modulus                          = 0,
                                mat2_lower_shear_modulus                         = 0,
                                mat2_lower_universal_anisotropy                  = 0,
                                mat2_lower_total_magnetization                   = 0,
                                mat2_lower_total_magnetization_normalized_volume = 0,
                                mat2_lower_e_ij                                  = 0,
                                mat2_upper_elec_cond_300k_low_doping             = 1e9,
                                mat2_upper_therm_cond_300k_low_doping            = 1e9,
                                mat2_upper_e_total                               = 1e9,
                                mat2_upper_e_ionic                               = 1e9,
                                mat2_upper_e_electronic                          = 1e9,
                                mat2_upper_n                                     = 1e9,
                                mat2_upper_bulk_modulus                          = 1e9,
                                mat2_upper_shear_modulus                         = 1e9,
                                mat2_upper_universal_anisotropy                  = 1e9,
                                mat2_upper_total_magnetization                   = 1e9,
                                mat2_upper_total_magnetization_normalized_volume = 1e9,
                                mat2_upper_e_ij                                  = 1e9)

    

