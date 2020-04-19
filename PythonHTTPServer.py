#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Filename: PythonHTTPServer.py
# Title: Sets up a local web server
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Sets up a local web server
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print ("serving at port", PORT)
httpd.serve_forever()

#httpd.shutdown
#httpd.server_close()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Scaling data to load onto the Globe
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Initialise scaler
MinMaxScaler = MinMaxScaler()

# Create dataframe and normalise sales to a near [0,1] range
Mag_df = pd.DataFrame({'Sales': [50, 94, 34, 14, 7]})
Mag_df['Sales_Norm'] = MinMaxScaler.fit_transform(Mag_df[['Sales']])+0.01
Mag_df