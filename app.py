from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>CarePlus Multi Speciality Hospital</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, sans-serif;
        }

        body{
            background:#f4f7fb;
            color:#333;
        }

        /* Header */

        header{
            background:#0077b6;
            color:white;
            padding:20px 40px;
            display:flex;
            justify-content:space-between;
            align-items:center;
            position:sticky;
            top:0;
            z-index:1000;
        }

        .logo{
            font-size:30px;
            font-weight:bold;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin-left:20px;
            font-size:18px;
        }

        nav a:hover{
            color:#90e0ef;
        }

        /* Hero Section */

        .hero{
            height:90vh;

            background:
            linear-gradient(rgba(0,0,0,0.5),
            rgba(0,0,0,0.5)),

            url('https://images.unsplash.com/photo-1586773860418-d37222d8fce3');

            background-size:cover;
            background-position:center;

            display:flex;
            justify-content:center;
            align-items:center;
            flex-direction:column;

            color:white;
            text-align:center;
            padding:20px;
        }

        .hero h1{
            font-size:65px;
        }

        .hero p{
            font-size:24px;
            margin-top:20px;
        }

        .hero button{
            margin-top:30px;
            padding:15px 40px;
            border:none;
            border-radius:10px;
            background:#00b4d8;
            color:white;
            font-size:18px;
            cursor:pointer;
        }

        .hero button:hover{
            background:#0077b6;
        }

        /* Emergency Banner */

        .emergency{
            background:red;
            color:white;
            text-align:center;
            padding:15px;
            font-size:20px;
            font-weight:bold;
        }

        /* Services */

        .section-title{
            text-align:center;
            margin:60px 0 30px;
            font-size:42px;
            color:#023e8a;
        }

        .services{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
            gap:25px;
            padding:20px 50px 60px;
        }

        .card{
            background:white;
            padding:30px;
            border-radius:15px;
            text-align:center;
            box-shadow:0px 5px 15px rgba(0,0,0,0.1);
            transition:0.3s;
        }

        .card:hover{
            transform:translateY(-10px);
        }

        .card h3{
            margin:15px 0;
            color:#0077b6;
        }

        .icon{
            font-size:50px;
        }

        /* Doctors */

        .doctors{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
            gap:25px;
            padding:20px 50px 60px;
        }

        .doctor-card{
            background:white;
            border-radius:15px;
            overflow:hidden;
            box-shadow:0px 5px 15px rgba(0,0,0,0.1);
            text-align:center;
        }

        .doctor-card img{
            width:100%;
            height:250px;
            object-fit:cover;
        }

        .doctor-card h3{
            margin-top:15px;
            color:#023e8a;
        }

        .doctor-card p{
            padding-bottom:20px;
        }

        /* Stats */

        .stats{
            background:#0077b6;
            color:white;
            display:flex;
            justify-content:space-around;
            flex-wrap:wrap;
            padding:60px 20px;
            text-align:center;
        }

        .stats h2{
            font-size:50px;
        }

        /* Appointment */

        .appointment{
            background:#caf0f8;
            padding:60px 20px;
        }

        form{
            max-width:600px;
            margin:auto;
            background:white;
            padding:30px;
            border-radius:15px;
            box-shadow:0px 5px 15px rgba(0,0,0,0.1);
        }

        form input,
        form select,
        form textarea{
            width:100%;
            padding:15px;
            margin:12px 0;
            border-radius:8px;
            border:1px solid #ccc;
        }

        form button{
            width:100%;
            padding:15px;
            background:#0077b6;
            color:white;
            border:none;
            border-radius:8px;
            font-size:18px;
            cursor:pointer;
        }

        form button:hover{
            background:#023e8a;
        }

        /* Testimonials */

        .testimonials{
            padding:60px 20px;
            text-align:center;
        }

        .testimonial-box{
            background:white;
            max-width:700px;
            margin:auto;
            padding:30px;
            border-radius:15px;
            box-shadow:0px 5px 15px rgba(0,0,0,0.1);
        }

        /* Footer */

        footer{
            background:#023e8a;
            color:white;
            text-align:center;
            padding:30px;
        }

        /* Scroll Button */

        #topBtn{
            position:fixed;
            bottom:20px;
            right:20px;
            display:none;
            background:#00b4d8;
            color:white;
            border:none;
            padding:15px;
            border-radius:50%;
            cursor:pointer;
            font-size:18px;
        }

        /* Responsive */

        @media(max-width:768px){

            header{
                flex-direction:column;
            }

            .hero h1{
                font-size:40px;
            }

            nav{
                margin-top:15px;
            }

        }

    </style>
</head>

<body>

<header>

    <div class="logo">🏥 CarePlus Hospital</div>

    <nav>
        <a href="#">Home</a>
        <a href="#services">Services</a>
        <a href="#doctors">Doctors</a>
        <a href="#appointment">Appointment</a>
        <a href="#contact">Contact</a>
    </nav>

</header>

<div class="emergency">
    🚑 Emergency Helpline: +91 9876543210
</div>

<section class="hero">

    <h1>Advanced Healthcare For Everyone</h1>

    <p>24/7 Emergency Services | Expert Doctors | Modern Facilities</p>

    <button onclick="scrollAppointment()">
        Book Appointment
    </button>

</section>

<h2 class="section-title" id="services">Our Services</h2>

<section class="services">

    <div class="card">
        <div class="icon">🚑</div>
        <h3>Emergency Care</h3>
        <p>24/7 emergency healthcare support.</p>
    </div>

    <div class="card">
        <div class="icon">🩺</div>
        <h3>Expert Doctors</h3>
        <p>Experienced specialists across all departments.</p>
    </div>

    <div class="card">
        <div class="icon">💊</div>
        <h3>Pharmacy</h3>
        <p>In-house pharmacy with quality medicines.</p>
    </div>

    <div class="card">
        <div class="icon">🧪</div>
        <h3>Laboratory</h3>
        <p>Advanced pathology and diagnostic services.</p>
    </div>

</section>

<h2 class="section-title" id="doctors">Our Doctors</h2>

<section class="doctors">

    <div class="doctor-card">
        <img src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=800&q=80">

        <h3>Dr. John Smith</h3>

        <p>Cardiologist</p>
    </div>

    <div class="doctor-card">
        <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=800&q=80">

        <h3>Dr. Sarah Johnson</h3>

        <p>Neurologist</p>
    </div>

    <div class="doctor-card">
        <img src="https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=800&q=80">

        <h3>Dr. David Lee</h3>

        <p>Orthopedic Specialist</p>
    </div>

</section>

<section class="stats">

    <div>
        <h2 id="patients">0</h2>
        <p>Patients Served</p>
    </div>

    <div>
        <h2 id="doctorsCount">0</h2>
        <p>Doctors</p>
    </div>

    <div>
        <h2 id="awards">0</h2>
        <p>Awards Won</p>
    </div>

</section>

<section class="appointment" id="appointment">

    <h2 class="section-title">Book Appointment</h2>

    <form onsubmit="submitForm(event)">

        <input type="text" placeholder="Enter Your Name" required>

        <input type="email" placeholder="Enter Email Address" required>

        <input type="tel" placeholder="Phone Number" required>

        <select required>

            <option value="">Select Department</option>

            <option>Cardiology</option>

            <option>Neurology</option>

            <option>Orthopedics</option>

            <option>General Medicine</option>

        </select>

        <textarea rows="4" placeholder="Describe Your Problem"></textarea>

        <button type="submit">Submit Appointment</button>

    </form>

</section>

<section class="testimonials">

    <h2 class="section-title">Patient Testimonials</h2>

    <div class="testimonial-box">

        <h3 id="testimonial-name">Rahul Sharma</h3>

        <p id="testimonial-text">
            Excellent hospital services and caring doctors.
        </p>

    </div>

</section>

<footer id="contact">

    <h3>📍 CarePlus Multi Speciality Hospital</h3>

    <p>Hyderabad, Telangana</p>

    <p>📞 +91 9876543210</p>

    <p>✉ careplus@hospital.com</p>

    <br>

    <p>© 2026 CarePlus Hospital. All Rights Reserved.</p>

</footer>

<button id="topBtn" onclick="topFunction()">⬆</button>

<script>

    // Scroll to appointment section

    function scrollAppointment(){

        document.getElementById("appointment").scrollIntoView({
            behavior:"smooth"
        });
    }

    // Appointment alert

    function submitForm(event){

        event.preventDefault();

        alert("✅ Appointment Booked Successfully!");
    }

    // Counter Animation

    function animateCounter(id, target){

        let count = 0;

        let speed = target / 100;

        let interval = setInterval(() => {

            count += speed;

            if(count >= target){

                count = target;

                clearInterval(interval);
            }

            document.getElementById(id).innerText =
            Math.floor(count) + "+";

        },20);
    }

    animateCounter("patients",15000);

    animateCounter("doctorsCount",120);

    animateCounter("awards",35);

    // Testimonials Slider

    let testimonials = [

        {
            name:"Rahul Sharma",
            text:"Excellent hospital services and caring doctors."
        },

        {
            name:"Priya Reddy",
            text:"Very clean hospital and supportive staff."
        },

        {
            name:"Kiran Kumar",
            text:"Quick emergency response and advanced facilities."
        }

    ];

    let index = 0;

    setInterval(() => {

        index = (index + 1) % testimonials.length;

        document.getElementById("testimonial-name").innerText =
        testimonials[index].name;

        document.getElementById("testimonial-text").innerText =
        testimonials[index].text;

    },3000);

    // Scroll Top Button

    let topBtn = document.getElementById("topBtn");

    window.onscroll = function(){

        if(document.body.scrollTop > 300 ||
           document.documentElement.scrollTop > 300){

            topBtn.style.display = "block";

        }else{

            topBtn.style.display = "none";
        }
    };

    function topFunction(){

        window.scrollTo({
            top:0,
            behavior:"smooth"
        });
    }

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
