from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files (directory to find 1SDMA.atm)
env.io.atom_files_directory = './:../atom_files'

a = automodel(env,
              alnfile  = 'bioinfo.pir',     # alignment filename
              knowns   = '1SDMA',              #id codes of the templates, used to find template file
              sequence = 'bioinfo')              # id code of the target (or quey)
a.starting_model= 1                 # index of the first model 
a.ending_model  = 1                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual homology modelling
