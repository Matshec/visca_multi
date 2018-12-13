from flask import Flask, render_template, Response
from flask_restful import reqparse, abort, Api, Resource
import core.visca_lib as visca
 

app = Flask( __name__ )
api = Api( app )

#creating camera object to serial port communication
camera = visca.D100( output='COM1' )
camera.init()

@app.route('/')
def home():
    return render_template('home.html')

parser = reqparse.RequestParser()
parser.add_argument( 'input', type=int )

class ViscaTest( Resource ):
    def get(self):
        #args = parser.parse_args()
        #input = args['input']
        #int_input = int(input)
        
        succes = camera.left(3)
        
        output_json = { 'was succesfull' : succes  }
        return output_json

def get_arg():
    args = parser.parse_args()
    input = args['input']
    return int(input)
    
class Up( Resource ):    
    def get(self):
        args = parser.parse_args()
        input = args['input']
        camera.up( input )
        return Response( home() , mimetype='text/html' )
    
class Down( Resource ):    
    def get(self):
        args = parser.parse_args()
        input = args['input']
        camera.down( input )
        return Response( home() , mimetype='text/html' )
    
class Left( Resource ):    
    def get(self):
        args = parser.parse_args()
        input = args['input']
        camera.left( input )
        return Response( home() , mimetype='text/html' )
    
class Right( Resource ):    
    def get(self):
        args = parser.parse_args()
        input = args['input']
        camera.right( input )
        return Response( home() , mimetype='text/html' )
    
class VHome( Resource ):    
    def get(self):
        camera.home()
        return Response( home() , mimetype='text/html' )
    
class Reset( Resource ):    
    def get(self):
        camera.reset()
        return Response( home() , mimetype='text/html' )
    
class FocusNear( Resource ):    
    def get(self):
        camera.focus_near()
        return Response( home() , mimetype='text/html' )
    
class ExposureAuto( Resource ):    
    def get(self):
        camera.exposure_full_auto()
        return Response( home() , mimetype='text/html' )

class Stop( Resource ):    
    def get(self):
        camera.stop()
        return Response( home() , mimetype='text/html' )         
    
# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource( ViscaTest, '/visca_test' )
api.add_resource( Up, '/up' )
api.add_resource( Down, '/down' )
api.add_resource( Right, '/right' )
api.add_resource( Left, '/left' )
api.add_resource( VHome, '/home' )
api.add_resource( Reset, '/reset' )
api.add_resource( FocusNear, '/focus_near' )
api.add_resource( ExposureAuto, '/exposure_auto' )
api.add_resource( Stop, '/stop' )

app.run(debug=False)