import time
import random
import pyautogui
from pynput.mouse import Listener
from sklearn.cluster import DBSCAN
import numpy as np


class MouseMovementPattern:
    def __init__(self, click_delay_record) -> None:
        self.click_delay_record = click_delay_record
        self.positions = []


class RandomClicker(MouseMovementPattern):
    def record_positions(self, clicking_time):
        start_time = time.time()

        while time.time() - start_time > clicking_time:
            self.positions.append(pyautogui.position())
            time.sleep(self.click_delay)
    
    def play_clicks(self, clicking_time):
        start_time = time.time()

        while time.time() - start_time > clicking_time:
            pyautogui.click(random.choice(self.positions))
            time.sleep(self.click_delay)


class ForwardClicker(MouseMovementPattern):

    def record_positions(self, clicking_time):

        start_time = time.time()
        self.last_click_time = 0

        def on_click(x, y, button, pressed):
            if pressed:
                current_time = time.time()
                time_difference = current_time - self.last_click_time

                self.positions.append((x, y, time_difference))
                self.last_click_time = current_time
        
        

        with Listener(on_click=on_click) as listener:
            while time.time() - start_time < clicking_time:
                pass
    
    def play_clicks(self, clicking_time):
        for i in range(len(self.positions)):
            pyautogui.click(self.positions[i][0], self.positions[i][1])
            
            if i != len(self.positions) - 1: 
                time.sleep(self.positions[i+1][2])



class FrequencyClusterClicker(MouseMovementPattern):
    def record_positions(self, clicking_time):
        start_time = time.time()

        while time.time() - start_time > clicking_time:
            self.positions.append(pyautogui.position())
            time.sleep(self.click_delay)
        
        points = np.array(self.positions)

        db = DBSCAN(eps=20, min_samples=4)
        cluster_labels = db.fit_predict(points)


        unique_clusters = np.unique(cluster_labels)
        cluster_points = {cluster: [] for cluster in unique_clusters}

        for i, label in enumerate(cluster_labels):
            cluster_points[label].append(list(points[i]))


        cluster_middle_point = [ [0,0] for i in range(len(unique_clusters))]

        for i in unique_clusters:
            sum_x, sum_y = (0, 0)
            for point in cluster_points[i]:

                sum_x += point[0]
                sum_y += point[1]

            cluster_middle_point[i][0] = int(sum_x/len(cluster_points[i]))
            cluster_middle_point[i][1] = int(sum_y/len(cluster_points[i]))
        
        self.positions = cluster_middle_point
    
    def play_clicks(self, clicking_time):
        start_time = time.time()

        while time.time() - start_time > clicking_time:
            pyautogui.click(random.choice(self.positions))
            time.sleep(self.click_delay)
