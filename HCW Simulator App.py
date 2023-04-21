import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import kv


def asinh(x):
    return np.arcsinh(x)
def newfunc(u, w):
    L1 = lambda y: kv(0, np.sqrt(w**2 + y**2))
    L, _ = quad(L1, 0, u)
    return L

def sph2cart(azimuth,elevation,r):
    x = r * np.cos(elevation) * np.cos(azimuth)
    y = r * np.cos(elevation) * np.sin(azimuth)
    z = r * np.sin(elevation)
    return x, y, z





# Define your pages
def page_home():
    st.write("Welcome to my app!")
    # Can add literature to the APP

def datainput():
    st.write(" Please input the data on this page for the Well")

 # Aquifer characteristics
    st.sidebar.subheader("Aquifer Characteristics")
    aquifer_type = st.sidebar.selectbox("Aquifer Type", ["Confined", "Unconfined"])
    if aquifer_type == "Confined" :
        aquifer_type=1
    if aquifer_type == "Unconfined" :
        aquifer_type=2
    B = st.sidebar.number_input("Thickness (L)", value=35.66)
    Kv = st.sidebar.number_input("Vertical Hydraulic Conductivity (L/T)", value=20)
    Kh = st.sidebar.number_input("Horizontal Hydraulic Conductivity (L/T)", value=20)
    Ss = st.sidebar.number_input("Specific Storage (L^-1)", value=1e-5)
    Sy = st.sidebar.number_input("Specific Yield", value=0.3)

    # For a leaky aquifer
    #st.sidebar.subheader("Leaky Aquifer")
    Kdash = st.sidebar.number_input("Conductivity of Aquitard", value=20)
    Bdash = st.sidebar.number_input("Thickness of Aquitard", value=100)
    numM = st.sidebar.number_input("Number of Points for Calculation", value=20)
    nterms = st.sidebar.number_input("Number of Terms in Summation", value=10)

    # Angled well
    st.sidebar.subheader("Angled Well")
    angled_well = st.sidebar.selectbox("Well Type", ["Horizontal", "Angled"])
    if angled_well == "Horizontal" :
        angled_well=1
    if angled_well == "Angled" :
        angled_well=2
    #beta = st.sidebar.number_input("Elevation Angle (Radians)", value=0.0)

    # Well
    st.sidebar.subheader("Well")
    x0 = st.sidebar.number_input("X-coordinate of Well Position (L)", value=300)
    y0 = st.sidebar.number_input("Y-coordinate of Well Position (L)", value=450)
    z0 = st.sidebar.number_input("Height of Laterals (L)", value=20)
    Q = st.sidebar.number_input("Well Pumping Rate (L^3/T)", value=1000)
    n_l = st.sidebar.number_input("Number of Laterals", value=1)
    L = []
    LS = []
    angle = []
    beta=[]
    st.sidebar.subheader("Lateral Data Input")
    for i in range(n_l):
        L.append(st.sidebar.number_input(f"Length of Lateral {i+1} (L)", value=500))
        LS.append(st.sidebar.number_input(f"Screened Length of Lateral {i+1} (L)", value=300))
        angle.append(st.sidebar.number_input(f"Azimuth Angle of Lateral {i+1} (Radians)", value=0.1))
        beta.append(st.sidebar.number_input(f"Beta Angle of well {i+1} (Radians)", value=0.1))
    r_c = st.sidebar.number_input("Radius of Caisson", value=0)
    t = st.sidebar.number_input("Time Since Start of Pumping (T)", value=365)

    # Mesh properties
    st.sidebar.subheader("Mesh Properties")
    z = st.sidebar.number_input("Height of Observation (L)", value=5)
    xmin = st.sidebar.number_input("Minimum X-Position of Mesh (L)", value=200)
    xmax = st.sidebar.number_input("Maximum X-Position of Mesh (L)", value=800)
    ymin = st.sidebar.number_input("Minimum Y-Position of Mesh (L)", value=300)
    ymax = st.sidebar.number_input("Maximum Y-Position of Mesh (L)", value=900)
    size = st.sidebar.number_input("Size of Grid Square (L)", value=50)
    
    progress_bar = st.progress(0)
    beta2=beta


#####################################


    x = np.arange(xmin, xmax+size, size)
    y = np.arange(ymin, ymax+size, size)
    x1,x2 = np.meshgrid(x, y)
    mat = np.zeros((len(y), len(x)))
    gesamt_absenkung = np.zeros((len(y), len(x)))
    ges2=np.zeros((int(x1.shape[0])*int(x1.shape[1])))
    s = np.zeros((len(y), len(x)))
    ges=[]
    leny=len(y)
    lenx=len(x)
 #print((type(x1)),x1,len(x1),len(x2[1]))
                                              #gesarr=np.array need to add an array 
    for j in range(n_l):
     #if(((j/n_l)*100)%5==0) :
     #print(((j/n_l)*100),'%')
        L_l = L[j]
        theta_i = angle[j]
        Beta = beta2[j]
     
        z = B - z
        z0 = B - z0
        probar=[]
        for i in range(x1.size):
            progress_bar.progress((j * x1.size + i + 1) / (n_l * x1.size))
            #if(int((i/x1.size)*100)%10==0) :
             #   if(int((i/x1.size)*100) not in probar) :
             
              #   st.write(int((i/x1.size)*100),'%')
               #  probar.append(int((i/x1.size)*100))
         # ------------------------- Hantush&Papadopolous --------------------------
            x = x1.flatten()[i]
            y = x2.flatten()[i]
         
            theta, r = math.atan2(y-y0, x-x0), math.sqrt((x-x0)**2 + (y-y0)**2)
         #print(theta,theta_i)
            sigma = r * math.cos(theta-theta_i) - r_c - L_l
            beta = r * math.sin(theta-theta_i)
            alpha = r * math.cos(theta-theta_i) - r_c
         
            if aquifer_type == 1:
                v_dash = Kh/Sy
            elif aquifer_type == 2:
                v_dash = Kh*B/Sy
        
            if t > 2.5*B**2/v_dash:
                u_1 = (alpha**2 + beta**2) / (4*v_dash*t)
                u_2 = (sigma**2 + beta**2) / (4*v_dash*t)
             #print(u_1,u_2)
             #print(math.log(u_1))
                if(u_1==0):
                 u_1=1
                 beta=1
                W_1 = -0.5772 - math.log(u_1) + u_1 - (u_1**2)/(2*math.factorial(2)) + (u_1**3)/(3*math.factorial(3)) - (u_1**4)/(4*math.factorial(4))
                W_2 = -0.5772 - math.log(u_2) + u_2 - (u_2**2)/(2*math.factorial(2)) + (u_2**3)/(3*math.factorial(3)) - (u_2**4)/(4*math.factorial(4))
            
                term_1 = alpha * W_1
                term_2 = sigma * W_2
                term_3 = 2 * L_l - 2*beta*(math.atan(alpha/beta) - math.atan(sigma/beta))
 

                if(u_1==0):
                 term_3=0
                 term_1=0
                 term_2=0
              
                if z == -1:
                    term_4 = 0
                else:
                   term_4 = 0
                   for n in range(1, 51):
                        term_4 += 1/n * (newfunc(n*math.pi*alpha/B, n*math.pi*beta/B) -
                                      newfunc(n*math.pi*sigma/B, n*math.pi*beta/B)) * \
                               math.cos(n*math.pi*z/B) * math.cos(n*math.pi*z0/B)
             
                mat = Q/L_l/4/math.pi/Kh/B * (term_1 - term_2 + term_3 + 4*B/math.pi * term_4)
        
            
            elif t <= B**2 / (20 * v_dash):
                w0 = z_i - z
                lambda0 = z_i + z
                thing = v_dash * t / B**2
             
                mat = Q / (4 * np.pi * K * L_l) * (asinh(alpha / np.sqrt(beta**2 + w0**2)) -
                    asinh(sigma / np.sqrt(beta**2 + w0**2)) + 
                 asinh(alpha / np.sqrt(beta**2 + lambda0**2)) - 
                 asinh(sigma / np.sqrt(beta**2 + lambda0**2)) -
                 2 * asinh(alpha / np.sqrt(beta**2 + (lambda0 + B*thing)**2)) +
                 2 * asinh(sigma / np.sqrt(beta**2 + (lambda0 + B*thing)**2)))
            else:
                print('Hantush not valid at this time')
 
        # print(gesamt_absenkung,gesamt_absenkung[i,j])
         #gesamt_absenkung[i,j]= gesamt_absenkung[i,j]+ mat
            ges.append(mat)
     
        ges2=np.array(ges)+ges2
        ges=[]
    
   

 #print(ges)
        

    gesamt_absenkung = np.array(ges2).reshape((int(x1.shape[0])),int(x1.shape[1]))



    fig, ax = plt.subplots(figsize=(8,4), subplot_kw=dict(aspect="equal"))

    # Create contour plot
    CS = ax.contour(x1, x2, gesamt_absenkung, linewidths=3, cmap='plasma',levels=10)
    plt.clabel(CS, inline=True, fontsize=10)

    # Plot the line
    for i in range(n_l):
        L_l = L[i]
        theta_i = angle[i]
        beta = beta2[i]

        XX, YY, ZZ = sph2cart(theta_i, beta, L_l)
        endx = x0 + XX
        endy = y0 + YY
        ax.plot([x0, endx], [y0, endy], color='k', linewidth=3, marker='o', markersize=10)

    # Set labels and title
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Contour plot with line")

    # Show plot
    st.pyplot(fig)






    
    return (aquifer_type, B, Kv, Kh, Ss, Sy, Kdash, Bdash, numM,nterms, angled_well, beta, x0, y0, z0, Q, n_l,L,LS,angle,r_c,t,z,xmin,xmax,ymin,ymax,size)


st.set_page_config(page_title='', layout='wide')
# Add custom CSS to change the background color
st.markdown(
    """
    <style>
    body {
        background-color: ##00c69b;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Create a menu with options to navigate between pages
aquifer_type = 1
menu = ["Data Input"]
choice = st.sidebar.radio("Select a page", menu)

# Show the appropriate page based on the user's choice
#if choice == "Home":
   # page_home()
if choice == "Data Input":
   aquifer_type, B, Kv, Kh, Ss, Sy, Kdash, Bdash, numM,nterms, angled_well, beta, x0, y0, z0, Q, n_l,L,LS,angle,r_c,t,z,xmin,xmax,ymin,ymax,size=datainput()
   #st.write(aquifer_type)
   #st.write(aquifer_type, B, Kv, Kh, Ss, Sy, Kdash, Bdash, numM,nterms, angled_well, beta, x0, y0, z0, Q, n_l,L,LS,angle,r_c,t,z,xmin,xmax,ymin,ymax,size)
#if choice == "Result" :

 #   st.write(aquifer_type, B, Kv, Kh, Ss, Sy, Kdash, Bdash, numM,nterms, angled_well, beta, x0, y0, z0, Q, n_l,L,LS,angle,r_c,t,z,xmin,xmax,ymin,ymax,size)

  #  result(aquifer_type, B, Kv, Kh, Ss, Sy, Kdash, Bdash, numM,nterms, angled_well, beta, x0, y0, z0, Q, n_l,L,LS,angle,r_c,t,z,xmin,xmax,ymin,ymax,size)


    
