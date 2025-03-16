from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import math
from kivy.clock import Clock

class  FRUSTRUM_MEASURES(BoxLayout):
    def __init__(self,app_instance, **kwargs):
        # Create the main layout
         super().__init__(orientation='vertical', **kwargs)
         self.padding=[5,5,5,5]
         self.app_instance = app_instance
         heading = Label(
            text="FRUSTRUM",
            font_size='32sp',  # Set font size
            bold=True,         # Make the text bold
            size_hint=(1,1) # Adjust size_hint for heading
            
        )
         self.add_widget(heading)
         back_button = Button(
            text="Back to Shape Selector",
            size_hint=(1, 0.2),
            padding=[2, 1],
            on_press=self.go_back,
        )
         self.add_widget(back_button)
          
        # Add other widgets below the heading (example: body text)
         body = Label(
            text=" calculate any measure of frustrum using this app ",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
         

         self.add_widget(body)
        # Create input fields for the two numbers
          
         self.input1 = TextInput(hint_text="Enter first first radius ", multiline=False, input_filter='float')
         self.input2 = TextInput(hint_text="Enter second  radius ", multiline=False, input_filter='float')
         self.input3= TextInput(hint_text="Enter height ", multiline=False, input_filter='float')
         self.input4 =TextInput(hint_text="Enter operation " )
        # Create a button to perform the addition
         add_button = Button(text="calculate", size_hint=(1, 0.3))
         add_button.bind(on_press=self.calculate_sum)
        
        # Create a label to display the result
         self.result_label = Label(text="Result will appear here", size_hint=(1, 0.3))
        
        # Add widgets to the layout
         self.add_widget(self.input1)
         self.add_widget(self.input2)
         self.add_widget(self.input3)
         self.add_widget(self.input4)
         self.add_widget(add_button)
         self.add_widget(self.result_label)

    def go_back(self, instance):
        # Call the main app's function to show the main screen
        self.app_instance.show_main_screen()      

    def calculate_sum(self, instance):
        try:
            # Get the numbers from the inputs
            radius1 = float(self.input1.text)
            radius2 = float(self.input2.text)
            height= float(self.input3.text)
            operation= str(self.input4.text).strip()
            pi  = math.pi
            squarius1 = math.pow( radius1, 2)
            squarius2= math.pow( radius2, 2)
            slant= height*height+ (squarius2-squarius1)
            slant1= math.sqrt( slant)

            if operation.lower()== "volume": 
              solutionV= 1/3*pi*height*(squarius1+squarius2+radius1*radius2)
              self.result_label.text = f"Result: {solutionV}"

            elif operation.lower().strip()== "slant height": 
               self.result_label.text = f"Result: { slant1}"
            elif operation.lower() == "curved surface area": 
             solutionCSA= pi*slant1*(radius1+radius2)
             self.result_label.text = f"Result: { solutionCSA}"

            elif operation.lower() == "total surface area": 
              solutionTSA= pi*(radius1+radius2)*slant1+pi*squarius1+pi*squarius2 
              self.result_label.text = f"Result: { solutionTSA}"

            else:
              print("invalid entry") 
    
            # Calculate the sum
            
            
            # Display the result
            
        except ValueError:
            # Handle invalid input
            self.result_label.text = "Error: Please enter valid numbers!"


class   CUBE_MEASURES( BoxLayout):
    def __init__(self,app_instance, **kwargs):
        # Create the main layout
         super().__init__(orientation='vertical', **kwargs)
         self.app_instance = app_instance
         heading = Label(
            text="CUBE",
            font_size='32sp',  # Set font size
            bold=True,         # Make the text bold
            size_hint=(1, 0.2) # Adjust size_hint for heading
        )
         self.add_widget(heading)
        
         back_button = Button(
            text="Back to Shape Selector",
            size_hint=(1, 0.2),
            on_press=self.go_back,
        )
         self.add_widget(back_button)
        # Add other widgets below the heading (example: body text)
         body = Label(
            text=" calculate any measure of cube ",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
         self.add_widget(body)
        # Create input fields for the two numbers
         self.input1 = TextInput(hint_text="Enter  measure of one side ", multiline=False, input_filter='float')
         self.input4 =TextInput(hint_text="Enter operation " )
        # Create a button to perform the addition
         add_button = Button(text="calculate", size_hint=(1, 0.3))
         add_button.bind(on_press=self.calculate_sum)
        
        # Create a label to display the result
         self.result_label = Label(text="Result will appear here", size_hint=(1, 0.3))
        
        # Add widgets to the layout
         self.add_widget(self.input1)
         self.add_widget(self.input4)
         self.add_widget(add_button)
         self.add_widget(self.result_label)

    def go_back(self, instance):
        # Call the main app's function to show the main screen
        self.app_instance.show_main_screen()            
         
    def calculate_sum(self, instance):
        try:
            # Get the numbers from the inputs
            sideCube = float(self.input1.text)
            operation= str(self.input4.text).strip()
            pi  = math.pi
            

            if operation.lower()== "volume": 
              solutionV=  sideCube*sideCube*sideCube
              self.result_label.text = f"Result: {solutionV}"

             
            elif operation.lower()=="surface area": 
             solutionCSA=  6*sideCube*sideCube
             self.result_label.text = f"Result: { solutionCSA}"

            elif operation.lower()=="lateral surface area": 
              solutionTSA= 4*sideCube*sideCube
              self.result_label.text = f"Result: { solutionTSA}"

            else:
              print("invalid entry") 
    
            # Calculate the sum
            
            
            # Display the result
            
        except ValueError:
            # Handle invalid input
            self.result_label.text = "Error: Please enter valid numbers!"


class   CUBOID_MEASURES( BoxLayout):
    def __init__(self,app_instance, **kwargs):
        # Create the main layout
         super().__init__(orientation='vertical', **kwargs)
         self.app_instance = app_instance
         heading = Label(
            text="CUBOID",
            font_size='32sp',  # Set font size
            bold=True,         # Make the text bold
            size_hint=(1, 0.2) # Adjust size_hint for heading
        )
         self.add_widget(heading)
         back_button = Button(
            text="Back to Shape Selector",
            size_hint=(1, 0.2),
            on_press=self.go_back,
        )
         self.add_widget(back_button)
        # Add other widgets below the heading (example: body text)
         body = Label(
            text=" calculate any measure of cuboid using this app ",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
         self.add_widget(body)
        # Create input fields for the two numbers
         self.input1 = TextInput(hint_text="Enter  length ", multiline=False, input_filter='float')
         self.input2 = TextInput(hint_text="Enter  breadth ", multiline=False, input_filter='float')
         self.input3= TextInput(hint_text="Enter height ", multiline=False, input_filter='float')
         self.input4 =TextInput(hint_text="Enter operation " ) 
        # Create a button to perform the addition
         add_button = Button(text="calculate", size_hint=(1, 0.3))
         add_button.bind(on_press=self.calculate_sum)
        
        # Create a label to display the result
         self.result_label = Label(text="Result will appear here", size_hint=(1, 0.3))
        
        # Add widgets to the layout
         self.add_widget(self.input1)
         self.add_widget(self.input2)
         self.add_widget(self.input3)
         self.add_widget(self.input4)
         self.add_widget(add_button)
         self.add_widget(self.result_label)
          

    def go_back(self, instance):
        # Call the main app's function to show the main screen
        self.app_instance.show_main_screen() 

    def calculate_sum(self, instance):
        try:
            # Get the numbers from the inputs
            length = float(self.input1.text)
            breadth = float(self.input2.text)
            height= float(self.input3.text)
            operation= str(self.input4.text).strip()
            pi  = math.pi
            squarius1 = math.pow(  length, 2)
            squarius2= math.pow(  breadth, 2)
            

            if operation.lower()== "volume": 
              solutionV= length*breadth*height
              self.result_label.text = f"Result: {solutionV}"

            
            elif operation.lower() =="surface area": 
             solutionCSA=  2*(length*breadth+length*height+breadth*height)
             self.result_label.text = f"Result: {  solutionCSA}"

            elif operation.lower() =="lateral surface area": 
              solutionTSA=  2*height*(length+breadth)
              self.result_label.text = f"Result: { solutionTSA}"

            else:
              print("invalid entry") 
    
            # Calculate the sum
            
            
            # Display the result
            
        except ValueError:
            # Handle invalid input
            self.result_label.text = "Error: Please enter valid numbers!"

class   SPHERE_MEASURES( BoxLayout):
    def __init__(self,app_instance, **kwargs):
        # Create the main layout
         super().__init__(orientation='vertical', **kwargs)
         self.app_instance = app_instance
         heading = Label(
            text=" SPHERE",
            font_size='32sp',  # Set font size
            bold=True,         # Make the text bold
            size_hint=(1, 0.2) # Adjust size_hint for heading
        )

         back_button = Button(
            text="Back to Shape Selector",
            size_hint=(1, 0.2),
            on_press=self.go_back,
        )
         self.add_widget(back_button)  
          
        # Add other widgets below the heading (example: body text)
         body = Label(
            text=" calculate any measure of sphere using this app ",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
         self.add_widget(body)
        # Create input fields for the two numbers
         self.input1 = TextInput(hint_text="Enter radius ", multiline=False, input_filter='float')
         self.input4 =TextInput(hint_text="Enter operation " )
        # Create a button to perform the addition
         add_button = Button(text="calculate", size_hint=(1, 0.3))
         add_button.bind(on_press=self.calculate_sum)
        
        # Create a label to display the result
         self.result_label = Label(text="Result will appear here", size_hint=(1, 0.3))
        
        # Add widgets to the layout
         self.add_widget(self.input1)
         self.add_widget(self.input4)
         self.add_widget(add_button)
         self.add_widget(self.result_label)
          
    def go_back(self, instance):
        # Call the main app's function to show the main screen
        self.app_instance.show_main_screen() 

    def calculate_sum(self, instance):
        try:
            # Get the numbers from the inputs
            radius1 = float(self.input1.text)
             
            operation= str(self.input4.text).strip()
            pi  = math.pi
            squarius1 = math.pow( radius1, 3)
            cubeius= math.pow( radius1, 2)
            

            if operation.lower()== "volume": 
              solutionV= 4/3*pi*squarius1
              self.result_label.text = f"Result: {solutionV}"

            elif operation.lower() =="surface area": 
              solutionTSA= pi*4*cubeius 
              self.result_label.text = f"Result: { solutionTSA}"

            else:
              print("invalid entry") 
    
            # Calculate the sum
            
            
            # Display the result
            
        except ValueError:
            # Handle invalid input
            self.result_label.text = "Error: Please enter valid numbers!"


class   CONE_MEASURES( BoxLayout):
   def __init__(self,app_instance,**kwargs):     
         super().__init__(orientation='vertical', **kwargs)
         self.app_instance = app_instance
         heading = Label(
            text="CONE",
            font_size='32sp',  # Set font size
            bold=True,         # Make the text bold
            size_hint=(1, 0.2) # Adjust size_hint for heading
        )
         back_button = Button(
            text="Back to Shape Selector",
            size_hint=(1, 0.5),
            on_press=self.go_back,
            halign='left',
            valign='middle'        )
         self.add_widget(back_button)

        # Add other widgets below the heading (example: body text)
         body = Label(
            text=" calculate any measure of cone using this app ",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
         self.add_widget(body)
        # Create input fields for the two numbers
         self.input1 = TextInput(hint_text="Enter radius ", multiline=False, input_filter='float')
         self.input3= TextInput(hint_text="Enter height ", multiline=False, input_filter='float')
         self.input4 =TextInput(hint_text="Enter operation " )
        # Create a button to perform the addition
         add_button = Button(text="calculate", size_hint=(1, 0.3))
         add_button.bind(on_press=self.calculate_sum)
        
        # Create a label to display the result
         self.result_label = Label(text="Result will appear here", size_hint=(1, 0.3))
        
        # Add widgets to the layout
         self.add_widget(self.input1)
         self.add_widget(self.input3)
         self.add_widget(self.input4)
         self.add_widget(add_button)
         self.add_widget(self.result_label)
 
         
   def go_back(self, instance):
        # Call the main app's function to show the main screen
        self.app_instance.show_main_screen()

    
     
   def calculate_sum(self, instance):
        try:
            # Get the numbers from the inputs
            radius1 = float(self.input1.text)
            height= float(self.input3.text)
            operation= str(self.input4.text).strip()
            pi  = math.pi
            squarius1 = math.pow( radius1, 2)
            slant= height*height+radius1*radius1
            slant1= math.sqrt( slant)

            if operation.lower()== "volume": 
              solutionV= 1/3*pi*height*squarius1
              self.result_label.text = f"Result: {solutionV}"

            elif operation.lower().strip()== "slant height": 
               self.result_label.text = f"Result: { slant1}"
            elif operation.lower() == "curved surface area": 
             solutionCSA= pi*slant1*radius1 
             self.result_label.text = f"Result: { solutionCSA}"

            elif operation.lower() == "total surface area": 
              solutionTSA= pi*radius1*(radius1+slant1) 
              self.result_label.text = f"Result: { solutionTSA}"

            else:
              print("invalid entry") 
    
            # Calculate the sum
            
            
            # Display the result
            
        except ValueError:
            # Handle invalid input
            self.result_label.text = "Error: Please enter valid numbers!"




class ShapeSelectorApp(App):
    def build(self):
        
        self.root_layout = BoxLayout(orientation="vertical")
        self.show_main_screen()  # Show the main screen initially
        return self.root_layout
 

    def show_main_screen(self):
        # Clear the root layout and display the main screen
        self.root_layout.clear_widgets()

        heading = Label(
            text="MESURATION",
            font_size="32sp",
            bold=True,
            size_hint=(1, 0.2),
        )
        self.root_layout.add_widget(heading)

        cone_button = Button(
            text="CONE",
            size_hint=(1, 0.2),
            on_press=self.show_cone_measures,
        )
        self.root_layout.add_widget(cone_button)

        frustrum_button = Button(
            text="FRUSTRUM",
            size_hint=(1, 0.2),
            on_press=self.show_frustrum_measures,
        )
        self.root_layout.add_widget(frustrum_button)

        sphere_button = Button(
            text="SPHERE",
            size_hint=(1, 0.2),
            on_press=self.show_sphere_measures,
        )
        self.root_layout.add_widget(sphere_button)

        cube_button = Button(
            text="CUBE",
            size_hint=(1, 0.2),
            on_press=self.show_cube_measures,
        )
        self.root_layout.add_widget(cube_button)
        
        cuboid_button = Button(
            text="CUBOID",
            size_hint=(1, 0.2),
            on_press=self.show_cuboid_measures,
        )
        self.root_layout.add_widget(cuboid_button)

    def show_cuboid_measures(self, instance=None):
        # Clear the root layout and display the cone measures screen
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(CUBOID_MEASURES(app_instance=self)) 


    def show_cube_measures(self, instance=None):
        # Clear the root layout and display the cone measures screen
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(CUBE_MEASURES(app_instance=self))


    def show_sphere_measures(self, instance=None):
        # Clear the root layout and display the cone measures screen
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(SPHERE_MEASURES(app_instance=self))


    def show_frustrum_measures(self, instance=None):
        # Clear the root layout and display the cone measures screen
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(FRUSTRUM_MEASURES(app_instance=self))

    def show_cone_measures(self, instance=None):
        # Clear the root layout and display the cone measures screen
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(CONE_MEASURES(app_instance=self))

 

    

   
    def on_circle_press(self, instance):
         self.root.clear_widgets()
         self.root.add_widget( FRUSTRUM_MEASURES())


    def on_square_press(self, instance):
         self.root.clear_widgets()
         self.root.add_widget(  CUBE_MEASURES())

    def on_triangle_press(self, instance):
         self.root.clear_widgets()
         self.root.add_widget( CONE_MEASURES())


    def on_rectangle_press(self, instance):
         self.root.clear_widgets()
         self.root.add_widget(  CUBOID_MEASURES())


    def on_pentagon_press(self, instance):
         self.root.clear_widgets()
         self.root.add_widget(  SPHERE_MEASURES())
    
    def switch_to_main_app(self):
        # Clear SubApp layout and return to MainApp
        self.root.clear_widgets()
        self.root.add_widget(self.layout)
    def switch_to_main(self):
        # Replace the SubApp layout with the main layout
        self.root.clear_widgets()
        self.root.add_widget(Button(
            text="Go to Sub App",
            size_hint=(1, 0.2),
            on_press=self.switch_to_sub
        ))  

    
if __name__ == "__main__":
    ShapeSelectorApp().run()
 