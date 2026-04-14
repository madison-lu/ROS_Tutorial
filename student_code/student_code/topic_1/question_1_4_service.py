import rclpy
from rclpy.node import Node
import pandas as pd
from tutorial_msgs.srv import GetBuoyLocation

class TutorialTopic_1_4_Service(Node):
    def __init__(self):
        super().__init__('question_1_4_service')
        self.tutorial_map = pd.DataFrame(
            columns=['type', 'x_loc', 'y_loc']
        )
        self.tutorial_map.loc[len(self.tutorial_map)] = {
            'type': 'red_buoy',
            'x_loc': 3.0,
            'y_loc': 4.0
        }
        self.tutorial_map.loc[len(self.tutorial_map)] = {
            'type': 'green_buoy',
            'x_loc': 0.0,
            'y_loc': -1.0
        }
        self.tutorial_map.loc[len(self.tutorial_map)] = {
            'type': 'black_buoy',
            'x_loc': 2.0,
            'y_loc': 10.0
        }
        self.tutorial_map.loc[len(self.tutorial_map)] = {
            'type': 'yellow_buoy',
            'x_loc': 1.0,
            'y_loc': -8.0
        }
        # TODO: Q1.4.b
        self.gate_side_information_service = self.create_service(
            ### STUDENT CODE HERE
                GetBuoyLocation,
                '/tutorial/get_buoy_location',
                self.handle_get_buoy_location
            ### END STUDENT CODE
        )
    
    def handle_get_buoy_location(self,
                                 request: GetBuoyLocation.Request,
                                 response: GetBuoyLocation.Response) -> None:
        desired_buoy = request.buoy_name
        # TODO: Q1.4.c
        ### STUDENT CODE HERE
        result = self.tutorial_map[self.tutorial_map['type'] == desired_buoy]
    
        if len(result) == 0:
            response.found = False
        else:
            response.found = True
            response.x_pos = result.iloc[0]['x_loc']
            response.y_pos = result.iloc[0]['y_loc']
        ### END STUDENT CODE
        return response

def main(args=None):
    rclpy.init(args=args)
    node = TutorialTopic_1_4_Service()
    rclpy.spin(node)