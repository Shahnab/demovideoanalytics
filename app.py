import streamlit as st
import pandas as pd

# Load data from CSV file
compare_df = pd.read_csv("compare.csv")

# Set app configuration to wide mode
st.set_page_config(page_title="Analysis Dashboard",layout="wide", initial_sidebar_state="auto")

st.markdown(
    """
    <style>
    body {
        color: black;
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True)

# Streamlit app layout
st.markdown("""<h1 style="color: red; text-align: center;">Badminton Match Analysis</h1>""", unsafe_allow_html=True)
st.markdown("""<h3 style="color: grey; text-align: center;">Powered by Gemini 1.5 Pro</h3>""", unsafe_allow_html=True)


# Create a two-column layout
col1, col2 = st.columns(2)

# Left Half (Comparison Table)
with col1:
    st.markdown("### Match Video")
    video_embed = f'<iframe src="https://www.youtube.com/embed/fIDRVN5JI1E" width="700" height="500" frameborder="0" allowfullscreen></iframe>'
    st.markdown(video_embed, unsafe_allow_html=True)
    st.markdown("### Match Details")
    st.markdown("The players in the match are:\n"
            "<ul>"
            "<li><span style='color:red;'>Lin Dan</span> from China</li>"
            "<li><span style='color:red;'>Jonathan Christie</span> from Indonesia</li>"
            "</ul>"
            "The video shows the final of the men's singles competition at the Barfoot & Thompson New Zealand Badminton Open.",
            unsafe_allow_html=True)

    st.markdown("### Comparison Table")
    st.table(compare_df)
    st.markdown("""
<h2 style='color: black;'>Summary of Lin Dan and Jonathan Christie's Playing Styles:</h2>

<p><b>Based on the video highlights, here's a comparative summary of Lin Dan and Jonathan Christie's playing styles:</b></p>

<h3 style='color: black;'>Lin Dan:</h3>
<ul>
<li><span style='color:red;'>Aggressive Smashing:</span> Known for his powerful and accurate smashes, often used as a finishing shot.</li>
<li><span style='color:red;'>Strong Defense:</span> Excellent defensive skills, retrieving opponents' attacks with agility and returning them with accuracy.</li>
<li><span style='color:red;'>Deceptive Shots:</span> Utilizes deceptive shots like drop shots and disguised net shots to catch opponents off guard.</li>
<li><span style='color:red;'>Experience and Tactical Awareness:</span> Employs strategic shot selection and court positioning based on his experience and tactical understanding.</li>
<li><span style='color:red;'>Mental Strength:</span> Possesses exceptional mental toughness and composure, remaining focused and confident in high-pressure situations.</li>
</ul>

<h3 style='color: black;'>Jonathan Christie:</h3>
<ul>
<li><span style='color:red;'>Dominant Smashing:</span> Employs powerful jump smashes and sharp half smashes to put opponents on the defensive and set up attacking opportunities.</li>
<li><span style='color:red;'>Deceptive Net Play:</span> Excels at net shots, utilizing tight net shots, disguised flicks, and quick net kills to catch opponents off guard.</li>
<li><span style='color:red;'>Agile Footwork:</span> Quick and precise footwork allows him to cover the court effectively and reach shots from various positions.</li>
<li><span style='color:red;'>Shot Variety:</span> Displays a diverse range of strokes, including drops, drives, and slices, making his attacks unpredictable.</li>
<li><span style='color:red;'>Mental Fortitude:</span> Maintains composure and focus throughout the match, demonstrating mental toughness and the ability to handle crucial points effectively.</li>
</ul>

<h3 style='color: black;'>Similarities:</h3>
<p>Both players possess strong attacking skills, utilize deception effectively, and demonstrate mental resilience. They are both highly skilled and experienced badminton players.</p>

<h3 style='color: black;'>Differences:</h3>
<p>Lin Dan's style is characterized by his exceptional defense and counter-attacking ability, while Christie relies more on his dominant smashing and agile footwork to dictate the pace of the game. Lin Dan's experience gives him a tactical edge, while Christie's youthful energy allows him to maintain a high level of intensity throughout the match.</p>

<p>It's important to note that these observations are based on the specific video highlights and may not represent the full range of their playing styles in all situations.</p>
""", unsafe_allow_html=True)


jonathan_christie_html = """
<h2 style="color: black;">Analysis of Jonathan Christie's Playing Style:</h2>

<p><b>Based on the video and commentary, here's an analysis of Jonathan Christie's playing style, focusing on the factors you mentioned:</b></p>

<h3 style="color: black;">Shot Distribution Analysis:</h3>
<p>Christie seems to favor attacking shots, particularly powerful smashes, especially directed towards his opponent's backhand.</p>
<p>He also uses cross-court shots effectively, but needs to be prepared for the subsequent diagonal movement.</p>
<p>He attempts drop shots, but makes some unforced errors on them, suggesting this might not be his strongest shot.</p>

<h3 style="color: black;">Shuttle Speed and Placement:</h3>
<p>Christie generally plays with high shuttle speed, aiming for quick rallies and putting pressure on his opponent.</p>
<p>His placement is generally accurate, but he can sometimes hit the shuttle wide or long.</p>

<h3 style="color: black;">Court Coverage:</h3>
<p>Christie demonstrates good court coverage, moving quickly and efficiently around the court.</p>
<p>He is particularly adept at moving forward to the net.</p>

<h3 style="color: black;">Shot Accuracy:</h3>
<p>Christie's shot accuracy is generally good, but he makes some unforced errors, especially on more difficult shots like drop shots.</p>
<p>He needs to improve his consistency to minimize these errors.</p>

<h3 style="color: black;">Rally Length and Endurance:</h3>
<p>Christie seems to prefer shorter rallies, aiming to finish points quickly with his powerful smashes.</p>
<p>His endurance appears good, but his strategy of quick rallies might be a way to conserve energy against more experienced players.</p>

<h3 style="color: black;">Service and Return Analysis:</h3>
<p>The video doesn't provide detailed information about Christie's service and return strategies.</p>
<p>However, there is a mention of him being cautioned by the umpire for not being ready to serve, suggesting he might be trying to speed up the pace between rallies.</p>

<h3 style="color: black;">Shot Velocity and Angle:</h3>
<p>Christie's shots, especially his smashes, have high velocity.</p>
<p>He uses a variety of angles, including cross-court and down-the-line shots, to keep his opponent off balance.</p>

<h3 style="color: black;">Error Analysis:</h3>
<p>Christie's main errors seem to be unforced errors, particularly on difficult shots like drop shots.</p>
<p>He also hits the shuttle wide or long at times. Minimizing these errors is crucial for improving his game.</p>

<h3 style="color: black;">Net Play:</h3>
<p>Christie demonstrates strong net play, especially on his forehand side.</p>
<p>He is quick to move forward and control the net area.</p>

<h3 style="color: black;">Tactical Analysis:</h3>
<p>Christie's main tactic seems to be playing aggressively and quickly, putting pressure on his opponent and aiming to finish points quickly.</p>
<p>He also tries to speed up the pace between rallies, which might be a strategy to disrupt his opponent's rhythm.</p>

<h3 style="color: black;">Player Style Classification:</h3>
<p>Christie can be classified as an aggressive, attacking player who relies on powerful smashes and quick rallies.</p>

<h3 style="color: black;">Match Flow and Momentum:</h3>
<p>Christie shows good fighting spirit and determination throughout the match.</p>
<p>He manages to build momentum in the second game, but loses it towards the end, allowing Lin Dan to take control and win the match.</p>

<h3 style="color: black;">Winning Shots Analysis:</h3>
<p>Christie's winning shots are primarily powerful smashes, often directed towards his opponent's backhand.</p>
<p>He also wins points with well-placed cross-court shots and net play.</p>

<h3 style="color: black;">Opponent-Specific Strategies:</h3>
<p>Christie's strategy against Lin Dan seems to be focused on keeping him on the court for as long as possible and disrupting his rhythm by playing quickly and speeding up the pace between rallies.</p>
<p>However, he is unable to consistently maintain this strategy and ultimately loses the match.</p>

<h3 style="color: black;">Overall:</h3>
<p>Jonathan Christie is a talented young player with a powerful and aggressive playing style. However, he needs to improve his consistency and shot selection to minimize unforced errors and compete more effectively against top players like Lin Dan.</p>
<p>This analysis is based on limited information from the video and commentary. A more comprehensive analysis would require studying more matches and statistics.</p>
"""


lin_dan_html = """
<h2 style="color: black;">Analysis of Lin Dan's Playing Style:</h2>

<p><b>Based on the video and commentary, here's an analysis of Lin Dan's playing style, focusing on the factors you mentioned:</b></p>

<h3 style="color: black;">Shot Distribution Analysis:</h3>
<p>Lin Dan displays a versatile shot selection, using a mix of attacking and defensive shots. He is particularly known for his deceptive drop shots, often played from around the head, and his trademark cross-court smash from his forehand side. He also uses lifts and clears effectively to set up his attacks.</p>

<h3 style="color: black;">Shuttle Speed and Placement:</h3>
<p>Lin Dan varies his shuttle speed, using both fast and slow shots to control the pace of the rallies and disrupt his opponent's rhythm. His placement is highly accurate, often placing the shuttle close to the lines or in difficult positions for his opponent to reach.</p>

<h3 style="color: black;">Court Coverage:</h3>
<p>Lin Dan has excellent court coverage, moving smoothly and efficiently around the court despite his age. He anticipates his opponent's shots well, allowing him to be in the right position to return them.</p>

<h3 style="color: black;">Shot Accuracy:</h3>
<p>Lin Dan's shot accuracy is exceptional. He rarely makes unforced errors and consistently places the shuttle in difficult positions for his opponent.</p>

<h3 style="color: black;">Rally Length and Endurance:</h3>
<p>Lin Dan is comfortable playing both long and short rallies. He can patiently build rallies and wait for the right opportunity to attack, or he can finish points quickly with his powerful smashes. His endurance is also excellent, allowing him to maintain his level of play throughout long matches.</p>

<h3 style="color: black;">Service and Return Analysis:</h3>
<p>Lin Dan has a strong and varied serve, using both low and high serves to keep his opponent guessing. His return of serve is also excellent, often putting pressure on his opponent from the start of the rally.</p>

<h3 style="color: black;">Shot Velocity and Angle:</h3>
<p>Lin Dan can generate high shot velocity, particularly on his smashes. He uses a wide variety of angles, including cross-court, down-the-line, and deceptive drop shots, to keep his opponent off balance.</p>

<h3 style="color: black;">Error Analysis:</h3>
<p>Lin Dan rarely makes unforced errors. His exceptional shot accuracy and control minimize his mistakes.</p>

<h3 style="color: black;">Net Play:</h3>
<p>Lin Dan has excellent net play, particularly on his backhand side. He can play delicate drop shots and control the net area effectively.</p>

<h3 style="color: black;">Tactical Analysis:</h3>
<p>Lin Dan's main tactic is controlling the pace and rhythm of the rallies. He uses a mix of attacking and defensive shots, varies his shuttle speed, and delays the game when necessary to disrupt his opponent's rhythm and create opportunities to attack.</p>

<h3 style="color: black;">Player Style Classification:</h3>
<p>Lin Dan can be classified as an all-around player who combines exceptional shot accuracy, control, and tactical awareness with the ability to play both offensively and defensively.</p>

<h3 style="color: black;">Match Flow and Momentum:</h3>
<p>Lin Dan demonstrates remarkable composure and experience throughout the match. He stays focused even when trailing and manages to regain momentum at crucial moments, ultimately winning the match.</p>

<h3 style="color: black;">Winning Shots Analysis:</h3>
<p>Lin Dan wins points with a variety of shots, including powerful smashes, deceptive drop shots, and well-placed clears and lifts. His ability to anticipate his opponent's shots and place the shuttle accurately contributes significantly to his success.</p>

<h3 style="color: black;">Opponent-Specific Strategies:</h3>
<p>Against Christie, Lin Dan uses his tactical experience to disrupt his opponent's rhythm and force him into making errors. He varies the pace of the rallies and uses his deceptive drop shots to counter Christie's aggressive attacks.</p>

<h3 style="color: black;">Overall:</h3>
<p>Lin Dan is a true badminton legend with an exceptional all-around game. His combination of shot accuracy, control, tactical awareness, and experience allows him to adapt his playing style to different opponents and remain at the top of his game.</p>
<p>This analysis is based on limited information from the video and commentary. A more comprehensive analysis would require studying more matches and statistics.</p>
"""

text_html = """
<h2 style="color: black;">Badminton Training Program:</h2>
<p><b>Inspired by Lin Dan and Jonathan Christie: Based on the strengths of both players, here's a badminton training program you can use to improve your skills with daily practice:</b></p>

<h3 style="color: black;">Warm-up (15 minutes):</h3>
<p>Light cardio: jogging, jumping jacks, skipping rope</p>
<p>Dynamic stretches: arm circles, leg swings, lunges with twists</p>
<p>Badminton-specific drills: shadow swings, footwork drills</p>

<h3 style="color: black;">Technical Skills (45 minutes):</h3>
<p>Shot accuracy and control: Practice hitting different shots (smashes, clears, drops, net shots) to specific targets on the court. Focus on consistency and accuracy rather than power.</p>
<p>Footwork: Perform footwork drills to improve your movement around the court, including forward, backward, and lateral movements. Practice split steps and quick changes of direction.</p>
<p>Net play: Practice different net shots (net kills, net lifts, net drops) and focus on controlling the net area. Improve your reflexes and reaction time at the net.</p>

<h3 style="color: black;">Match Play and Tactical Practice (30 minutes):</h3>
<p>Play practice matches against different opponents to apply your skills in a competitive setting. Focus on specific tactics, such as controlling the pace of the rallies, exploiting your opponent's weaknesses, and anticipating their shots.</p>
<p>Try to incorporate elements of both Lin Dan's and Jonathan Christie's playing styles into your game.</p>

<h3 style="color: black;">Cool-down and Stretching (10 minutes):</h3>
<p>Light cardio: walking, slow jogging</p>
<p>Static stretches: focus on major muscle groups used during badminton</p>

<p><b>Additional Tips:</b></p>
<ul>
<li>Practice regularly: Aim for daily practice, even if it's just for a short period. Consistency is key to improvement.</li>
<li>Record your practice sessions: This can help you identify areas where you need to improve and track your progress.</li>
<li>Get coaching: Consider getting coaching from a qualified badminton coach to receive personalized feedback and guidance.</li>
<li>Watch professional badminton matches: Observe how top players like Lin Dan and Jonathan Christie play and try to learn from their techniques and tactics.</li>
<li>Stay motivated and have fun: Badminton should be enjoyable. Focus on your progress and celebrate your successes.</li>
</ul>

<p><b>Remember: This is just a sample training program. You may need to adjust it based on your individual skill level, fitness, and goals. It's important to listen to your body and take rest days when needed. By practicing regularly and focusing on your weaknesses, you can develop your badminton skills and become a more competitive player.</b></p>
"""
# Right Half (Tabs)
with col2:
    st.markdown("### Analysis")
    tab1, tab2, tab3 = st.tabs(["Christie's Style", "Lin's Style", "Training Program"])
    with tab1:
        st.markdown(jonathan_christie_html, unsafe_allow_html=True)
    with tab2:
        st.markdown(lin_dan_html, unsafe_allow_html=True)
    with tab3: 
        st.write(text_html, unsafe_allow_html=True)
