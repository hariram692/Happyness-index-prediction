

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components


# loading the saved models

student_model = pickle.load(open('C:/Users/admin/3D Objects/happyness index prediction/student.sav', 'rb'))

parent_model = pickle.load(open('C:/Users/admin/3D Objects/happyness index prediction/parent.sav','rb'))

teacher_model = pickle.load(open('C:/Users/admin/3D Objects/happyness index prediction/teacher.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Happy index prediction using ml',
                          
                          [ 'Home',
                            'student prediction',
                           'parent prediction',
                           'teacher prediction',
                           'School Rankings',
                            'Feedback',
                            'chat graph'],
                          default_index=0)

# Diabetes Prediction Page
if (selected == 'Home'):
    
    page_bg_img= """
    <style>
    [data-testid="stAppViewContainer"]{ 
    background-image:url("https://images.unsplash.com/photo-1472289065668-ce650ac443d2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1169&q=80");
    background-size:cover;
    }
    [data-testid="stMarkdownContainer"]{
    
    color:"Red"
    }
    
    </style>
    """
    st.markdown(page_bg_img,unsafe_allow_html=True)
    

    # page title
    # st.title('STUDENT HAPPINESS INDEX')
    st.markdown("<h1 style='text-align: center;'>STUDENT HAPPINESS INDEX</h1>",unsafe_allow_html=True)
    st.markdown(
        "<p style='box-shadow: 0 0 3px 3px white;'text-align:center;'>'The happiness of students is a crucial aspect of their academic journey.It is widely acknowledged that students who are happy and satisfied with their educational experience are more likely to perform better academically, have higher levels of engagement, and develop positive attitudes towards learning. In contrast, unhappy students are more likely to struggle academically, experience stress, and have lower levels of motivation.  Furthermore, the happiness of students extends beyond academic performance. It can also impact their social and emotional development, their overall well-being, and even their future success in life. Therefore, it is essential to recognize the importance of student happiness and take measures to promote it within the education system. </p>",unsafe_allow_html=True)
    
    
  
    
# Student Prediction Page
if (selected == 'student prediction'):
    
    # page title
    st.title("STUDENT'S HAPPINESS PREDICTION")
    
    
    # Questionnaire
    st.write("""##### 1. Rate the quality of education ?   
    Enter 0 : Easy  
    Enter 1 : Hard  
    Enter 2 : Moderate""")
    Levels = st.text_input("Below enter your option.", key=1)

    st.write("""##### 2. Type of environment in the school ?   
    Enter 0 : Assessment Centered  
    Enter 1 : Knowledge Centered  
    Enter 2 : Learner Centered""")
    Environment = st.text_input("Below enter your option.", key=2)

    st.write("""##### 3. Does Teachers have competitive nature ?   
    Enter 0 : Highly  
    Enter 1 : Moderately  
    Enter 2 : Not at all""")
    Competitive = st.text_input("Below enter your option.", key=3)

    st.write("""##### 4. What are the number of teaching classes per day ?   
    Enter 0 : 6  
    Enter 1 : 8  
    Enter 2 : 10""")
    Classes = st.text_input("Below enter your option.", key=4)

    st.write("""##### 5. Are they providing enough facilities for laboratory ?   
    Enter 0 : No  
    Enter 1 : Not Always  
    Enter 2 : Yes""")
    Lab = st.text_input("Below enter your option.", key=5)

    st.write("""##### 6. How many hours are allocated to the sports ?   
    Enter 0 : 2-3 Hours weekly  
    Enter 1 : 4-5 Hours weekly  
    Enter 2 : 6-8 Hours weekly""")
    Sports = st.text_input("Below enter your option.", key=6)

    st.write("""##### 7. What is the condition of the toilets ?   
    Enter 0 : Badly Maintained  
    Enter 1 : Better  
    Enter 2 : Hygiene""")
    Toilet = st.text_input("Below enter your option.", key=7)

    st.write("""##### 8. Are there any sports competetions in the school ?   
    Enter 0 : Never  
    Enter 1 : Sometimes  
    Enter 2 : Yes""")
    Sports_Competition = st.text_input("Below enter your option.", key=8)

    st.write("""##### 9. How many students per class ?   
    Enter 0 : 20-30  
    Enter 1 : 30-40  
    Enter 2 : 40-50""")
    Students_per_class = st.text_input("Below enter your option.", key=9)

    st.write("""##### 10. In which langugae does teachers teach and communicate ?   
    Enter 0 : English  
    Enter 1 : Hindi  
    Enter 2 : Telugu""")
    Langugae = st.text_input("Below enter your option.", key=10)

    st.write("""##### 11. What are the timings of the school ?   
    Enter 0 : 5 hrs  
    Enter 1 : 6 hrs  
    Enter 2 : 7 hrs""")
    Timings	 = st.text_input("Below enter your option.", key=11)

    st.write("""##### 12. How frequently parent-teacher meetings are held ?   
    Enter 0 : Annually  
    Enter 1 : Half-yearly  
    Enter 2 : Quarterly""")
    Meetings = st.text_input("Below enter your option.", key=12)

    st.write("""##### 13. How frequently cultural fests are organised in a year ?   
    Enter 0 : Never  
    Enter 1 : Once a year  
    Enter 2 : Twice a year""")
    Fests = st.text_input("Below enter your option.", key=13)

    st.write("""##### 14. How many field trips in a year ?   
    Enter 0 : Never  
    Enter 1 : Once  
    Enter 2 : Twice""")
    Field_trips	 = st.text_input("Below enter your option.", key=14)

    st.write("""##### 15. Is clean & filtered water facility available ?   
    Enter 0 : Never  
    Enter 1 : Once  
    Enter 2 : Twice""")
    Water = st.text_input("Below enter your option.", key=15)

    st.write("""##### 16. Is mid day meal scheme part of your school ?   
    Enter 0 : No  
    Enter 1 : Yes""")
    Mid_day_meal = st.text_input("Below enter your option.", key=16)

    st.write("""##### 17. How is the quality of Food ?   
    Enter 0 : Can be improved  
    Enter 1 : Excellent  
    Enter 2 : Good""")
    Quality_of_food	= st.text_input("Below enter your option.", key=17)

    st.write("""##### 18. How frequently assessment exams are conducted ?   
    Enter 0 : Monthly  
    Enter 1 : Never  
    Enter 2 : Weekly""")
    Assessment = st.text_input("Below enter your option.", key=18)

    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('student Result'):
        student_prediction = student_model.predict([[Levels, Environment, Competitive, Classes, Lab, Sports,
        Toilet, Sports_Competition, Students_per_class, Langugae,
        Timings, Meetings, Fests, Field_trips, Water, Mid_day_meal,
        Quality_of_food, Assessment]])

        st.success('The output is {}'.format(student_prediction ))
        
        
        
# Heart Disease Prediction Page
if (selected == 'parent prediction'):
    
    # page title
    st.title("PARENT'S HAPPINESS PREDICTION")
    
    #Questionnaire
    st.write("""##### Unnamed: 0   
    Enter 0 : Always  
    Enter 1 : Sometimes  
    Enter 2 : Never""")
    Unnamed0 = st.text_input("Below enter your options.")

    st.write("""##### 1. Rate the quality of education ?   
    Enter 0 : 1-3  
    Enter 1 : 4-7  
    Enter 2 : 8-10""")
    Quality = st.text_input("Below enter your option.", key=1)

    st.write("""##### 2. Are the teachers well educated ?   
    Enter 0 : Highly  
    Enter 1 : Moderately  
    Enter 2 : Poorly""")
    Teacher_Quality = st.text_input("Below enter your option.", key=2)

    st.write("""##### 3. Did the school management provide books on time ?   
    Enter 0 : Always  
    Enter 1 : Sometimes  
    Enter 2 : Never""")
    Books = st.text_input("Below enter your option.", key=3)

    st.write("""##### 4. How are the classrooms maintained?   
    Enter 0 : Clean  
    Enter 1 : Not Bad  
    Enter 2 : Dirty""")
    Classroom = st.text_input("Below enter your option.", key=4)

    st.write("""##### 5. Rate the quality of the food ?   
    Enter 0 : 1-3  
    Enter 1 : 4-7  
    Enter 2 : 8-10""")
    Food = st.text_input("Below enter your option.", key=5)

    st.write("""##### 6. Is the school giving too much work to your child ?   
    Enter 0 : Yes  
    Enter 1 : Not Always  
    Enter 2 : No""")
    Homework= st.text_input("Below enter your option.", key=6)

    st.write("""##### 7. Does your child feel comfortable in understanding the subjects ?   
    Enter 0 : Yes  
    Enter 1 : Sometimes  
    Enter 2 : No""")
    Understanding_subs	= st.text_input("Below enter your option.", key=7)

    st.write("""##### 8. How often do they conduct Parent-Teacher meetings ?   
    Enter 0 : Quarterly  
    Enter 1 : Half-yearly  
    Enter 2 : Annually""")
    Meetings = st.text_input("Below enter your option.", key=8)

    st.write("""##### 9. Would you like to join your child in the same school next year ?   
    Enter 0 : Yes  
    Enter 1 : No""")
    Continue_school= st.text_input("Below enter your option.", key=9)    
    
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Parent Result'):
        parent_prediction = parent_model.predict([[Unnamed0, Quality, Teacher_Quality, Books, Classroom,
        Food, Homework, Understanding_subs, Meetings, Continue_school,
       ]])                          
        
        
        st.success('The output is {}'.format(parent_prediction ))
    
    

# Teacher Prediction Page
if (selected == "teacher prediction"):
    
    # page title
    st.title("TEACHER'S HAPPINESS PREDICTION")
    
    #Questionnaire
    st.write("""##### 1. Is salary being given on time ?   
    Enter 0 : Always  
    Enter 1 : Never  
    Enter 2 : Sometimes""")
    Salary = st.text_input("Below enter your option.", key=1)

    st.write("""##### 2. What about the teaching and learning process ?  
    Enter 0 : Moderately-designed  
    Enter 1 : Poorly-designed  
    Enter 2 : Well-designed""")
    Learning = st.text_input("Below enter your option.", key=2)

    st.write("""##### 3. How is the infrastructure ?  
    Enter 0 : Excellent  
    Enter 1 : Good  
    Enter 2 : Poor""")
    Infra = st.text_input("Below enter your option.", key=3)

    st.write("""##### 4. Teaching experience  
    Enter 0 : 0-5 years  
    Enter 1 : 5-10 years  
    Enter 2 : 10+ years""")                      
    Experience = st.text_input("Below enter your option.", key=4)

    st.write("""##### 5. How long have you been working in the same school ?  
    Enter 0 : 0-5 years  
    Enter 1 : 5-10 years  
    Enter 2 : 10+ years""")
    School = st.text_input("Below enter your option.", key=5)

    st.write("""##### 6. Is teaching done on activity based ?  
    Enter 0 : Always  
    Enter 1 : Never  
    Enter 2 : Sometimes""")
    Activity_based = st.text_input("Below enter your option.", key=6)

    st.write("""##### 7. How well can students speak and understand English ?  
    Enter 0 : Better  
    Enter 1 : Excellent  
    Enter 2 : Poor""")
    English= st.text_input("Below enter your option.", key=7)

    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Teacher result"):
        teacher_prediction = teacher_model.predict([[Salary, Learning, Infra, Experience, School, Activity_based,
        English]])                          
        
        st.success('The output is {}'.format(teacher_prediction ))


if(selected == 'School Rankings'):
    st.header("STUDENT'S HAPPINESS INDEX - SCHOOL WISE RANKINGS")


    Table = """
<style>
    #one {
  width: 100%;
  }
  table,tr,th,td{
    border: 3px solid whitesmoke;
    border-collapse: collapse;
    padding: 10px;
    font-size: 15px;
    color: white;
    background: linear-gradient(top,#3c3c3c 0%,#222222 100%);
    background: -webkit-linear-gradient(top,#3c3c3c 0%,#222222 100%);
}
th{
    background-color: darkgray;
}
th:hover{
    background: purple;
}
td:hover{
    background: orange;
}

</style>
<table id="one">
  <thead>
    <th>Rank</th>
    <th>School</th>
    <th>Area</th>
    <th>Happiness Index</th>
  </thead>
  <tr>
    <td class="rank"># 1</td>
    <td>Govt High School</td>
    <td>Ameerpet</td>
    <td>12.437</td>
  </tr>
  <tr>
    <td class="rank"># 2</td>
    <td>Govt High School</td>
    <td>Yousufguda</td>
    <td>12.258</td>
  </tr>
  <tr>
    <td class="rank"># 3</td>
    <td>Govt High School</td>
    <td>Erramanzil</td>
    <td>12.181</td>
  </tr>
  <tr>
    <td class="rank"># 4</td>
    <td>Zilla Parishad High School</td>
    <td>Nizampet</td>
    <td>11.714</td>
  </tr>
  <tr>
    <td class="rank"># 5</td>
    <td>Zilla Parishad High School</td>
    <td>Yellamabanda</td>
    <td>11.541</td>
  </tr>
  <tr>
    <td class="rank"># 6</td>
    <td>Zilla Parishad High School</td>
    <td>Miyapur</td>
    <td>11.224</td>
  </tr>
  <tr>
    <td class="rank"># 7</td>
    <td>Zilla Parishad High School</td>
    <td>Anjaiah Nagar</td>
    <td>10.945</td>
  </tr>
  <tr>
    <td class="rank"># 8</td>
    <td>Zilla Parishad High School</td>
    <td>KPHB</td>
    <td>10.811</td>
  </tr>
  <tr>
    <td class="rank"># 9</td>
    <td>Zilla Parishad High School</td>
    <td>Kukatpally</td>
    <td>10.755</td>
  </tr>
  <tr>
    <td class="rank"># 10</td>
    <td>Zilla Parishad High School</td>
    <td>Bachupally</td>
    <td>10.507</td>
  </tr>
  <tr>
    <td class="rank"># 11</td>
    <td>Zilla Parishad High School</td>
    <td>Jagathgirigutta</td>
    <td>10.222</td>
  </tr>
  <tr>
    <td class="rank"># 12</td>
    <td>Zilla Parishad High School</td>
    <td>Bollaram</td>
    <td>10.087</td>
  </tr>
  <tr>
    <td class="rank"># 13</td>
    <td>Zilla Parishad High School</td>
    <td>Pragati Nagar</td>
    <td>10.046</td>
  </tr>
  <tr>
    <td class="rank"># 14</td>
    <td>Zilla Parishad High School</td>
    <td>Mallampet</td>
    <td>9.995</td>
  </tr>
  <tr>
    <td class="rank"># 15</td>
    <td>Zilla Parishad High School</td>
    <td>Sanath Nagar</td>
    <td>9.981</td>
  </tr>
  <tr>
    <td class="rank"># 16</td>
    <td>Zilla Parishad High School</td>
    <td>Kairathabad</td>
    <td>9.797</td>
  </tr>
  <tr>
    <td class="rank"># 17</td>
    <td>Zilla Parishad High School</td>
    <td>Vengal Rao Colony</td>
    <td>9.772</td>
  </tr>
  <tr>
    <td class="rank"># 18</td>
    <td>Zilla Parishad High School</td>
    <td>Hyder Nagar</td>
    <td>9.534</td>
  </tr>
  <tr>
    <td class="rank"># 19</td>
    <td>Zilla Parishad High School</td>
    <td>Mominpet</td>
    <td>9.016</td>
  </tr>
  <tr>
    <td class="rank"># 20</td>
    <td>Zilla Parishad High School</td>
    <td>Kohir</td>
    <td>9.000</td>
  </tr>
  <tr>
    <td class="rank"># 21</td>
    <td>Zilla Parishad High School</td>
    <td>Marpally</td>
    <td>8.832</td>
  </tr>
  <tr>
    <td class="rank"># 22</td>
    <td>Zilla Parishad High School</td>
    <td>Sadasivpet</td>
    <td>8.774</td>
  </tr>
</table>
"""
    st.markdown(Table, unsafe_allow_html=True)


# Feedback
if (selected == 'Feedback'):
    
    # page title
    st.title('Common Findings from Survey')

    English_medium = """
    <div>
    <h3 style="color:#ffd12b;">Necessity of English as the medium of Instructions in the school.</h3>
    </div>
    <p>
    There are several potential benefits of using English as the medium of instruction in schools:

Improved communication skills: By learning in English, students are exposed to a wider range of vocabulary and grammar structures, which can help them develop better communication skills in both spoken and written English. This can be especially important for students who may want to pursue further education or careers in international settings.

Access to global information and resources: English is the language of international business, science, and technology, and many of the most important publications and resources in these fields are in English. By learning in English, students can access a wider range of information and resources, which can help them stay up-to-date with the latest developments in their fields of study.

Better job opportunities: English is often a requirement for many high-paying jobs, especially those in multinational corporations or in industries that require frequent international travel. By learning in English, students can improve their chances of securing these types of jobs and building successful careers.

Increased cultural awareness: English is a widely spoken language, and learning it can help students better understand and appreciate different cultures and perspectives. This can help them become more open-minded and tolerant individuals, which can be valuable both in their personal and professional lives.

Enhanced academic performance: In some cases, learning in English can lead to better academic performance, as students may be more motivated to learn and engage with the material when it is presented in a language that is more widely recognized and respected.

Overall, while there may be some challenges associated with learning in English, the potential benefits of doing so can be significant for students and their future success.
    </p>
    """
    st.markdown(English_medium,unsafe_allow_html=True)

    Food_quality = """
    <div>
    <h3 style="color:#ffd12b;">Improve the Quality of Food.</h3>
    </div>
    <p>
    According to teachers, parents and students, the food been served to the government school students is of low quality and very unhygienic. The rice which is served is also not cooked properly. Most of the schools do not have proper supply of safe drinking water and some do not provide soaps for children to wash their hands. Proper sanitisation is not maintained in the school premises, mainly the kitchen.
    Improving the quality of food in schools is an important goal, as it can have a significant impact on the health and well-being of students. Here are some potential strategies for achieving this:

Offer more fresh, whole foods: One of the best ways to improve the quality of food in schools is to offer more fresh, whole foods, such as fruits, vegetables, and whole grains. These foods are typically lower in calories and higher in nutrients than processed foods and can help students maintain a healthy weight and reduce their risk of chronic diseases.

Reduce or eliminate processed foods: Many processed foods, such as sugary snacks and high-fat, high-sodium meals, are not only unhealthy but can also lead to decreased academic performance and concentration. By reducing or eliminating these foods from school menus, students may be more likely to stay focused and engaged in their studies.

Partner with local farms and producers: Another way to improve the quality of food in schools is to partner with local farms and producers to provide fresh, locally sourced foods. This can help support the local economy while also ensuring that students have access to high-quality, fresh foods.

Provide nutrition education: In addition to offering healthy food options, it's also important to educate students about the importance of good nutrition and healthy eating habits. This can include classes or workshops on nutrition, cooking demonstrations, or other educational activities that help students understand the link between their diet and their health.

Involve students in menu planning: Finally, involving students in menu planning can be an effective way to improve the quality of food in schools. This can help ensure that the foods offered are appealing to students while also providing an opportunity to teach them about healthy eating habits and food preparation.
    </p>
    """
    st.markdown(Food_quality,unsafe_allow_html=True)

    Drinking_water = """
    <div>
        <h3 style="color:#ffd12b;">Providing Cleaned & Filtered drinking water facility.</h3>
    </div>
    <p>
According our Survey 95'%' of the schools doesn't provide drinking water facility to the students.
Providing drinking water facilities in schools has several potential benefits for students and staff, including:

Improved hydration: Drinking enough water is essential for staying hydrated and maintaining good health. When water is easily accessible, students are more likely to drink it throughout the day, which can help prevent dehydration, headaches, fatigue, and other negative health outcomes.

Better academic performance: Studies have shown that dehydration can negatively impact cognitive function, including memory, attention, and concentration. By providing drinking water facilities, schools can help ensure that students are properly hydrated, which may lead to better academic performance and classroom engagement.

Reduced absenteeism: Dehydration and other water-related illnesses can lead to absenteeism and missed school days. By providing access to clean drinking water, schools can help reduce the risk of these illnesses and ensure that students are able to attend school regularly.

Improved behavior and mood: Dehydration can also lead to irritability, anxiety, and other negative mood states. By ensuring that students have access to clean drinking water throughout the day, schools can help promote positive behavior and improve overall mood and well-being.

Enhanced overall health: Drinking water is essential for good health and can help prevent a wide range of illnesses and health conditions, including obesity, diabetes, and kidney disease. By providing access to clean drinking water, schools can help promote overall health and well-being for their students and staff.

In summary, providing drinking water facilities in schools has several potential benefits for students and staff, including improved hydration, better academic performance, reduced absenteeism, improved behavior and mood, and enhanced overall health.
    </p>
    """   
    st.markdown(Drinking_water,unsafe_allow_html=True)

    Competitive_teachers = """
    <div>
        <h3 style="color:#ffd12b;">Teachers should have right competitive attitude and positive approach.</h3>
    </div>
    <p>
    While some level of competition can be healthy and motivating in any profession, there are some potential benefits and drawbacks of having a competitive nature in teachers. Here are some potential benefits:

Increased student engagement and motivation: Teachers who are competitive may be more likely to challenge themselves and their students to achieve higher levels of academic success. This can lead to increased engagement and motivation among students, as they strive to meet the high standards set by their teacher.

Improved academic performance: When teachers are competitive, they may be more likely to implement innovative teaching methods or find ways to help their students achieve better academic outcomes. This can result in improved academic performance among students.

Professional growth and development: Teachers who are competitive may be more likely to seek out professional development opportunities, attend conferences, or engage in research and collaboration with other educators. This can lead to ongoing professional growth and development, which can benefit both the teacher and their students.

Recognition and rewards: Teachers who are competitive may be more likely to be recognized for their achievements and receive rewards or accolades for their hard work. This can help boost their confidence and motivation, and may inspire them to continue to strive for excellence in their teaching.
    </p>
    """
    st.markdown(Competitive_teachers,unsafe_allow_html=True)



# describtion
if (selected == 'chat graph'):
    
    # page title
    st.title('chat graph')

    st.text('fuyuygugu')

    

if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")




