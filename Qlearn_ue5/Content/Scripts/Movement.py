from mlpluginapi import MLPluginAPI
import unreal_engine as ue
import random  # Import random module

class Movement(MLPluginAPI):
 
    def on_json_input(self, input=None):
        if input is None:
            # Generate a random default value if no input is provided
            value = random.uniform(1.5, 10.5)  # Random float between 1 and 100
            ue.log(f"No input received. Using default random value: {value}")
        else:
            try:
                #if value was number 
                value = float(input)  # recive value intiger or float 
            except:
                ue.log("Input is not a number.")
                return {'result': 'Invalid input'}

        ue.log(f'Initial Value: {value}')

        # loop icreasing number (2.5 time )
        for _ in range(5):
            value += 2.5
        

        ue.log(f'Final Value after loop: {value}')

        return {
            'result': value
        }

def get_api():
    return Movement.get_instance()