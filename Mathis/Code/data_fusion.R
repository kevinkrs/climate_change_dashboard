# Clean environment #
rm(list=ls())

# Import #

annual_co_emissions_by_region <- read_csv("Desktop/Dashboard/Data/Situation_annual-co-emissions-by-region.csv")
fossil_fuel_consumption_by_fuel_type <- read_csv("Desktop/Dashboard/Data/Situation_fossil-fuel-consumption-by-fuel-type.csv")
renewable_energy_gen <- read_csv("Desktop/Dashboard/Data/Situation_renewable-energy-gen.csv")
renewable_share_energy <- read_csv("Desktop/Dashboard/Data/Situation_renewable-share-energy.csv")
world_population_by_world_regions_post_1820 <- read_csv("Desktop/Dashboard/Data/Situation_world-population-by-world-regions-post-1820.csv")

# Selection #

colnames(fossil_fuel_consumption_by_fuel_type) = c("Entity", "Code", "Year", "Coal", "Gas", "Oil")
Coal_consumption = fossil_fuel_consumption_by_fuel_type %>% dplyr::select(Entity, Year, Coal)
Gas_consumption = fossil_fuel_consumption_by_fuel_type %>% dplyr::select(Entity, Year, Gas)
Oil_consumption = fossil_fuel_consumption_by_fuel_type %>% dplyr::select(Entity, Year, Oil)
rm(fossil_fuel_consumption_by_fuel_type)

colnames(renewable_energy_gen) = c("Entity", "Code", "Year", "Biomass", "Hydro", "Solar", "Wind")
Biomass_generation = renewable_energy_gen %>% dplyr::select(Entity, Year, Biomass)
Hydro_generation = renewable_energy_gen %>% dplyr::select(Entity, Year, Hydro)
Solar_generation = renewable_energy_gen %>% dplyr::select(Entity, Year, Solar)
Wind_generation = renewable_energy_gen %>% dplyr::select(Entity, Year, Wind)
rm(renewable_energy_gen)

colnames(annual_co_emissions_by_region) = c("Entity", "Code", "Year", "CO2_emissions")
co_emissions = annual_co_emissions_by_region %>% dplyr::select(Entity, Year, CO2_emissions)
rm(annual_co_emissions_by_region) 

colnames(renewable_share_energy) = c("Entity", "Code", "Year", "Renewables")
renewable_energy = renewable_share_energy %>% dplyr::select(Entity, Year, Renewables)
rm(renewable_share_energy)

colnames(world_population_by_world_regions_post_1820) = c("Entity", "Code", "Year", "Population")
Population = world_population_by_world_regions_post_1820 %>% dplyr::select(Entity, Year, Population)
rm(world_population_by_world_regions_post_1820)

# Filter year #

Biomass_generation = Biomass_generation %>% dplyr::filter(Year > 1980 & Year < 2020)
co_emissions = co_emissions %>% dplyr::filter(Year > 1980 & Year < 2020)
Coal_consumption = Coal_consumption %>% dplyr::filter(Year > 1980 & Year < 2020)
Gas_consumption = Gas_consumption %>% dplyr::filter(Year > 1980 & Year < 2020)
Hydro_generation = Hydro_generation %>% dplyr::filter(Year > 1980 & Year < 2020)
Oil_consumption = Oil_consumption %>% dplyr::filter(Year > 1980 & Year < 2020)
Population = Population %>% dplyr::filter(Year > 1980 & Year < 2020)
renewable_energy = renewable_energy %>% dplyr::filter(Year > 1980 & Year < 2020)
Solar_generation = Solar_generation %>% dplyr::filter(Year > 1980 & Year < 2020)
Wind_generation = Wind_generation %>% dplyr::filter(Year > 1980 & Year < 2020)

# Filter Entity #

Biomass_generation = Biomass_generation %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
co_emissions = co_emissions %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
Coal_consumption = Coal_consumption %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
Gas_consumption = Gas_consumption %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
Hydro_generation = Hydro_generation %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
Oil_consumption = Oil_consumption %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
Population = Population %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
renewable_energy = renewable_energy %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
Solar_generation = Solar_generation %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")
Wind_generation = Wind_generation %>% dplyr::filter(Entity != "Asia Pacific" & Entity != "CIS" & Entity != "Central America" & Entity != "Eastern Africa" & Entity != "Europe (other)" & Entity != "Middle Africa" & Entity != "Middle East" & Entity != "Other Asia & Pacific" & Entity != "Other CIS" & Entity != "Other Caribbean" & Entity != "Other Middle East"  & Entity != "Other Northern Africa" & Entity != "Other South America" & Entity != "Other Southern Africa" & Entity != "South & Central America" & Entity != "USSR" & Entity != "Western Africa")

# Harmonization #

co_emissions$indice = str_c(co_emissions$Entity, as.character(co_emissions$Year))
data_fusion = data.frame(indice = str_c(Biomass_generation$Entity, as.character(Biomass_generation$Year)),x = 1)
co_emissions = left_join(co_emissions, data_fusion, by = "indice", copy = T)
co_emissions = co_emissions %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Biomass_generation$indice = str_c(Biomass_generation$Entity, as.character(Biomass_generation$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Biomass_generation = left_join(Biomass_generation, data_fusion, by = "indice", copy = T)
Biomass_generation = Biomass_generation %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Coal_consumption$indice = str_c(Coal_consumption$Entity, as.character(Coal_consumption$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Coal_consumption = left_join(Coal_consumption, data_fusion, by = "indice", copy = T)
Coal_consumption = Coal_consumption %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Gas_consumption$indice = str_c(Gas_consumption$Entity, as.character(Gas_consumption$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Gas_consumption = left_join(Gas_consumption, data_fusion, by = "indice", copy = T)
Gas_consumption = Gas_consumption %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Hydro_generation$indice = str_c(Hydro_generation$Entity, as.character(Hydro_generation$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Hydro_generation = left_join(Hydro_generation, data_fusion, by = "indice", copy = T)
Hydro_generation = Hydro_generation %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Oil_consumption$indice = str_c(Oil_consumption$Entity, as.character(Oil_consumption$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Oil_consumption = left_join(Oil_consumption, data_fusion, by = "indice", copy = T)
Oil_consumption = Oil_consumption %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

renewable_energy$indice = str_c(renewable_energy$Entity, as.character(renewable_energy$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
renewable_energy = left_join(renewable_energy, data_fusion, by = "indice", copy = T)
renewable_energy = renewable_energy %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Solar_generation$indice = str_c(Solar_generation$Entity, as.character(Solar_generation$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Solar_generation = left_join(Solar_generation, data_fusion, by = "indice", copy = T)
Solar_generation = Solar_generation %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Wind_generation$indice = str_c(Wind_generation$Entity, as.character(Wind_generation$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Wind_generation = left_join(Wind_generation, data_fusion, by = "indice", copy = T)
Wind_generation = Wind_generation %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

Population$indice = str_c(Population$Entity, as.character(Population$Year))
data_fusion = data.frame(indice = str_c(co_emissions$Entity, as.character(co_emissions$Year)),x = 1)
Population = left_join(Population, data_fusion, by = "indice", copy = T)
Population = Population %>% dplyr::filter(x == 1) %>% dplyr::select(-indice,-x)
rm(data_fusion)

# By Population #

co_emissions$CO2_emissions = (co_emissions$CO2_emissions/Population$Population)*1000000000
Biomass_generation$Biomass = (Biomass_generation$Biomass/Population$Population)*1000000000
Hydro_generation$Hydro = (Hydro_generation$Hydro/Population$Population)*1000000000
Solar_generation$Solar = (Solar_generation$Solar/Population$Population)*1000000000
Wind_generation$Wind = (Wind_generation$Wind/Population$Population)*1000000000
Coal_consumption$Coal = (Coal_consumption$Coal/Population$Population)*1000000000
Gas_consumption$Gas = (Gas_consumption$Gas/Population$Population)*1000000000
Oil_consumption$Oil = (Oil_consumption$Oil/Population$Population)*1000000000

# Format 1 #

Biomass_generation$Indicator = colnames(Biomass_generation)[3]
Biomass_generation = Biomass_generation %>% dplyr::select(Entity, Indicator, Year, Biomass)
colnames(Biomass_generation) = c("Country_Name", "Indicator_Name", "Year", "Value")

co_emissions$Indicator = colnames(co_emissions)[3]
co_emissions = co_emissions %>% dplyr::select(Entity, Indicator, Year, CO2_emissions)
colnames(co_emissions) = c("Country_Name", "Indicator_Name", "Year", "Value")

Coal_consumption$Indicator = colnames(Coal_consumption)[3]
Coal_consumption = Coal_consumption %>% dplyr::select(Entity, Indicator, Year, Coal)
colnames(Coal_consumption) = c("Country_Name", "Indicator_Name", "Year", "Value")

Gas_consumption$Indicator = colnames(Gas_consumption)[3]
Gas_consumption = Gas_consumption %>% dplyr::select(Entity, Indicator, Year, Gas)
colnames(Gas_consumption) = c("Country_Name", "Indicator_Name", "Year", "Value")

Hydro_generation$Indicator = colnames(Hydro_generation)[3]
Hydro_generation = Hydro_generation %>% dplyr::select(Entity, Indicator, Year, Hydro)
colnames(Hydro_generation) = c("Country_Name", "Indicator_Name", "Year", "Value")

Oil_consumption$Indicator = colnames(Oil_consumption)[3]
Oil_consumption = Oil_consumption %>% dplyr::select(Entity, Indicator, Year, Oil)
colnames(Oil_consumption) = c("Country_Name", "Indicator_Name", "Year", "Value")

Solar_generation$Indicator = colnames(Solar_generation)[3]
Solar_generation = Solar_generation %>% dplyr::select(Entity, Indicator, Year, Solar)
colnames(Solar_generation) = c("Country_Name", "Indicator_Name", "Year", "Value")

Wind_generation$Indicator = colnames(Wind_generation)[3]
Wind_generation = Wind_generation %>% dplyr::select(Entity, Indicator, Year, Wind)
colnames(Wind_generation) = c("Country_Name", "Indicator_Name", "Year", "Value")

renewable_energy$Indicator = colnames(renewable_energy)[3]
renewable_energy = renewable_energy %>% dplyr::select(Entity, Indicator, Year, Renewables)
colnames(renewable_energy) = c("Country_Name", "Indicator_Name", "Year", "Value")

dataset <- rbind(Biomass_generation, Hydro_generation, Solar_generation, Wind_generation, 
                 Coal_consumption, Gas_consumption, Oil_consumption,
                 co_emissions, renewable_energy)

dataset = dataset %>% dplyr::arrange(Year, Country_Name)
colnames(dataset) = c("Country Name", "Indicator Name", "Year", "Value")

# Export #
write.csv(x = dataset, file = "data_situation.csv")





