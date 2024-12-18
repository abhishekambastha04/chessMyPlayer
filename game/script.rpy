# The script of the game goes in this file.
default sana_powers = {
    "patience": 10,
    "aggression": 10,
    "tactics": 10,
    "skill": 10,
    "memory": 10,
    "confidence": 10
}

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image sanaSprite = im.Scale("sanaaa_sp.png", 490, 460)
image dadSprite = im.Scale("pops.png", 500, 500) 
image connorSprite = im.Scale("prof_connor.png", 420, 520)
image carterSprite = im.Scale("connor_sprite.png", 520, 520)
image joseySprite = im.Scale("joseySprite.png", 470, 420)
image momSprite = im.Scale("sana_mom.png", 500, 500)

define sana = Character("Sana", color = "#8c2a23", what_font = "FacultyGlyphic-Regular.ttf")
define profConnor = Character("Professor Connor", color = "#1f39bf")
define carter = Character("Carter", color= "#107832", what_font="SourGummy_Expanded-Regular.ttf")
define steve = Character("steve", color = "#730348", what_font = "Raleway-Black.ttf")
define Josey = Character("Josey", color = "#6d1f91", what_font = "Raleway-Black.ttf")
define Anatoly = Character("Anatoly", color = "#294a2d")

image anatolySprite = im.Scale("dad_chess_story.png", 520, 480)

default sana_signed_up = False # variable for if she signs up for tournament

# scene background images
image bg_game = im.Scale("game_background.jpg", 1920, 1080)
image bg_class = im.Scale("classroom.jpg", 1920, 1080)
image bg_street = im.Scale("street.jpg", 1920, 1080)
image bg_diner = im.Scale("dinertable.png", 1920, 1080)
image bg_library_day = im.Scale("library_bg.jpeg", 1920, 1080)
image lunchroom = im.Scale("lunch.jpg", 1920, 1080)
image exiting_school = im.Scale("exitingschool.jpg", 1920, 1080)
image bg_bedroom = im.Scale("bgbedroom.jpeg", 1920, 1080)
image bg_chess_board = im.Scale("chess_sana.jpg", 1920, 1080)
image bg_living_room = im.Scale("bg_livingg_room.jpeg", 1920, 1080)
image paper = im.Scale("paper_bg.jpg", 1920, 1080)
image bg_basement = im.Scale("bg_basement.jpg", 1920, 1080)
image bg_chess_room = im.Scale("chess_room.jpg", 1920, 1080)
image bg_tournament = im.Scale("bgtourneyhall.jpg", 1920, 1080)
image bg_park_bench = im.Scale("parkbench.jpg", 1920, 1080)
image bg_porch = im.Scale("porch_story.jpeg", 1920, 1080)

image puzz_1 = im.Scale("puzzle1.png", 400, 400)
image puzz_2 = im.Scale("puzzle2.png", 400, 400)
image puzz_3 = im.Scale("puzzle3.jpg", 400, 400)
image bookk = im.Scale("chessbook.jpg", 650, 400)

label start:
    scene bg_game
    play music "chess_thinking.mp3" loop
    "Welcome to {color=#8c2a23}{b}Checkmate Chronicles{/b}{/color}, a tale of ambition, resilience, and the power of the mind."
    "Step into the shoes of Sana, a young prodigy growing up in the tense backdrop of the Cold War. From the bustling chatter of a 1970s classroom to the hallowed halls of international chess tournaments, your choices will shape her destiny."
    "Will Sana rise to the challenge, mastering both the board and the complexities of life, or will the weight of her world prove too much to bear? The journey is yours to navigate."
    "Brace yourself for a story of strategy, sacrifice, and self-discovery, where every move counts."
    
    # Proceed with the story
    "Your {i}journey{/i} begins now..."
    jump intro_scene
    
label intro_scene:
    scene bg_class
    show connorSprite at right
    profConnor "DECORUM! Decorum. I notice that some of you have been lacking in your homeworks lately. Accordingly, please put your bagpacks up front immediately as we have a pop quiz to take."
    carter "Not again. This is like the third day in a row. Come on."
    profConnor "Best you do not speak again Carter. Will I have to call your parents again?"
    "Professor Connor walks around, handing out tests."
    profConnor "Sana, you seem fuzzled. Is everything alright at home?"
    show sanaSprite at left
    sana "Yes, of course."
    profConnor "Good luck on the test."
    # central idea is that as sana progresses, she will do more of these tasks and gain points which will help her beat the final chess bot at the end because the difficulty of the chess bot goes down as you gain more points
    # mini game of mental math questions
    stop music
    jump start_math_quiz
    
    
label lunch_announcement:
    scene lunchroom with fade

    "Alright students before we break for lunch, let's take a quick look at what's happening in the world right now."
    "The Cold War is in full swing between the United States and the Soviet Union, with tensions rising every day."
    "Some say we're standing on the brink of something catastrophic, but others {b}think this 'cold' conflict might never turn hot.{/b}"
    "Either way, it's shaping the world, and we can't ignore it. Now, go ahead and enjoy your lunch, but think about how these global events might affect us in the future."
    "Alright, that's enough for today. Remember to be back on time for the next lesson! Go grab some food, everyone!"
    show carterSprite at left
    carter "Hear that commie? It is your people."
    steve "I swear to god. Its the same stuff every time."
    carter "I have been saying this. I don't get how they let them into our land when their people want war."
    carter "Its people like this that are ruining our country"
    show joseySprite at right
    Josey "SHHHHHHHH. Oh my god guys. Grow up. We are not 8 anymore."
    Josey "Just cause she is from there does not mean... "
    carter "Literally just say your one of them. Weird ass. I don't get why you defend them so much. Maybe, maybee.. you should"
    steve "Move there then Josey!"
    Josey "God! You guys are so immature. Bye."
    hide carterSprite
    hide joseySprite
    jump exiting_school
    
label exiting_school:
    scene exiting_school with dissolve
    play music "game_theme.mp3" fadeout 1.0 fadein 1.0 loop
    Josey "Hi Sana! Hey, I'm really sorry about what happened earlier in class."
    show sanaSprite at left
    sana "Oh, hi Josey. It's alright, really."
    show joseySprite at right
    Josey "No, it's not. They were being total jerks, and I should have said something. I hate seeing you treated like that."

    Josey "Anyway, how did the math quiz go for you? I know you were worried about it yesterday."
    sana "It went fine."
    Josey "Are you sure? You seem kind of... distracted."

    Josey "I'm really sorry about everything today. Is there anything I can do to make you feel better?"
    Josey "I could walk home with you? Or we could grab something sweet from the diner. My treat!"

    menu:
        "Open up to Josey about the quiz":
            sana "Actually, the quiz was harder than I expected. I don't think I did very well."
            sana "And... honestly, what they said at lunch really got to me. It's just been a rough day."
            Josey "Oh, Sana, I'm so sorry. I really should have stood up for you."
            Josey "How about this? Let's grab milkshakes at the diner. You can vent to me about anything. My treat."
            sana "Thanks for offering but I cannot. I have to home."
            jump diner_scene

        "Brush it off and decline Josey's offer":
            sana "No, really, it’s fine. I don’t want to bother you with it."
            Josey "You’re not bothering me, Sana. You know I’m here for you, right?"
            sana "Yeah, I know. Thanks, Josey, but I think I just need some time to myself today."
            Josey "Okay, but if you need anything, you can always call me, alright?"
            sana "I will."
            jump walking_home_alone
    hide joseySprite
            
label walking_home_alone:
    scene bg_street
    show sanaSprite at right
    sana "I know Josey was just trying to help, but I didn't want to drag her into my mess."
    sana "I'll figure it out on my own. I always do."
    jump diner_scene

label diner_scene:
    scene bg_diner
    show sanaSprite at left
    play music "game_theme.mp3" fadeout 1.0 fadein 1.0 loop
    "The soft creak of the {color=#964B00}wooden floor{/color} announced Dad's arrival before he appeared in the doorway. His familiar silhouette, slightly stooped yet steady, was framed by the warm glow of the hallway light."
    "The rhythmic ticking of the clock on the wall suddenly seemed louder, each second stretching as if to mark his entrance."
    "As he stepped into the room, the clock chimed crisply, the sharp sound cutting through the quiet hum of the evening. 6:15 PM—right on the dot, as always." 
    "Dad's routine was as precise as the clock itself, and tonight was no exception. The faint aroma of dinner drifted through the house, mingling with the cool autumn air that seeped in through the cracks in the old windowpanes."
    show dadSprite at right
    "Dad" "How was school today?"
    sana "It was fine, Dad."
    "Dad" "Hmm. Was there a quiz today in math? I know Professor Connor has been pushing you hard."
    
    menu:
        "Lie and say there was no quiz":
            sana "No, not today. Just more homework as usual."
            "Dad" "Keep focusing. I want to see you succeed, not waste your time like your classmates."
            sana "Yes, Dad."
        
        "Tell the truth about the quiz":
            sana "Yes, there was a quiz... It was okay, I guess."
            "Dad" "But 'okay' is not enough. You must be better than okay. Remember, hard work is the key to everything. Understand?"
            sana "I understand."
            "Dad" "No you do not. You never have."

    "Dad sighed, his sharp eyes softening slightly as he walked to the table. The faint clink of plates being arranged punctuated the otherwise quiet house."
    
    "Dad" "Let's eat. I made Borscht and pelmeni."
    "The steaming bowls of deep-red borscht filled the air with the earthy aroma of beets and dill. Beside them, a plate of plump, golden pelmeni dumplings sat invitingly, glistening with a light sheen of butter."
    
    "Dad" "You know, today on the radio they spoke about Reagan and his arms race. Always the Americans trying to push us Russians. He doesn't understand strength, only noise."
    "Sana poked at her food, her appetite dwindling as the conversation veered into politics."
    sana "Do we have to talk about this, Dad?"
    "Dad" "Why not? This is important. You must understand your heritage. The world is divided, Sana. You cannot ignore it."
    
    "The conversation shifted to the weather—how the chill of autumn reminded Dad of his childhood winters in St. Petersburg. But the warmth of nostalgia was short-lived."
    sana "Did Mom call?"
    stop music
    "The room grew colder despite the steaming bowls of food. Dad's expression hardened."
    "Dad" "Нет. And we will not discuss this. Eat your food."
    
    "The rest of the meal passed in silence, save for the occasional clatter of utensils against plates. Sana kept her head down, her thoughts far from the table."
    "After dinner, Dad moved to the living room, flipping on the TV to a Russian news channel. The anchor's voice was clipped and sharp, reporting on the latest tensions in the Cold War."
    "As the smell of tobacco filled the house, Sana watched her father light a cigarette, the ember glowing like a dull, angry star in the dim room."
    
    sana "I'll be upstairs."
    "Dad" "Sleep soon."
    
    "Sana climbed the creaking stairs to her room, the muffled sound of the news fading behind her. Her sanctuary awaited, quiet and untouched by the tensions downstairs."
    
    $ next_scene = "breakfast"
    jump diary_scene

# Initialize persistent diary entries if they don't exist
default persistent.diary_entries = []
init python:
    def format_diary_date():
        """Returns formatted current date for diary entries"""
        import datetime
        return datetime.datetime.now().strftime("%B %d, %Y")
    
    def add_diary_entry(entry_text):
        """Adds a new diary entry with date and formatting"""
        if entry_text and entry_text.strip():
            dated_entry = f"{format_diary_date()}\n\n{entry_text.strip()}"
            persistent.diary_entries.append(dated_entry)
            return True
        return False

style diary_text:
    font "handwriting.ttf" 
    size 42
    color "#000000"
    line_spacing 4

label diary_scene:
    scene bg_bedroom with dissolve
    play music "piano.mp3" fadeout 1.0 fadein 1.0 loop
    show sanaSprite at left
    "Sana sat at her small desk, the faint glow of her desk lamp casting long shadows across the room. Outside, the wind whispered through the trees, a gentle contrast to the chaos of her thoughts."
    "She opened her diary, its worn pages filled with sketches, scribbles, and the private musings of a girl navigating a complicated world."
    
    # Main diary interaction loop
    label diary_menu:
        menu:
            "What would you like to do?"
            "Write a new entry":
                $ new_entry = renpy.input("What would you like to write in your diary?", length=500)
                
                if add_diary_entry(new_entry):
                    "Sana carefully wrote her thoughts down, her pen moving steadily across the page."
                    "Entry added to diary."
                else:
                    "Sana stared at the empty page, unable to find the words."
                
                jump diary_menu

            "Read past entries" if persistent.diary_entries:
                $ entry_index = 0
                
                label read_entries:
                    if entry_index < len(persistent.diary_entries):
                        scene bg_bedroom with dissolve
                        show screen diary_page(persistent.diary_entries[entry_index])
                        
                        menu:
                            "What would you like to do?"
                            
                            "Next entry" if entry_index < len(persistent.diary_entries) - 1:
                                $ entry_index += 1
                                jump read_entries
                            
                            "Previous entry" if entry_index > 0:
                                $ entry_index -= 1
                                jump read_entries
                            
                            "Return to diary menu":
                                hide screen diary_page
                                jump diary_menu
                    
                    jump diary_menu

            "Read past entries" if not persistent.diary_entries:
                "The diary pages were blank, a silent reminder of the thoughts she hadn't yet written."
                jump diary_menu

            "Close diary":
                "Sana closed her diary, carefully placing it back in its special spot."
                stop music fadeout 1.0
                sana "Best I sleep now or dad will get upset."
                jump expression next_scene
                
    return

# Define the diary page screen
screen diary_page(entry_text):
    add "black" alpha 0.3
    frame:
        background "#fff8dc"
        xsize 1200         
        ysize 800        
        xalign 0.5
        yalign 0.6
        padding (40, 40)  
        
        # Add drop shadow effect
        at transform:
            matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.05) * SaturationMatrix(1.2)
        
        viewport:
            mousewheel True    
            draggable True      
            scrollbars "vertical"
            yinitial 0.0      
            
            vbox:
                spacing 20     
                text entry_text:
                    style "diary_text"
                    xalign 0.0  
                    text_align 0.0
                    xsize 1100 
                    line_spacing 20
                    
label breakfast:
    scene bg_diner with dissolve
    show sanaSprite at left
    
    "The morning sunlight streamed through the kitchen window, casting golden streaks on the modest breakfast table. Sana sat quietly, a bowl of steaming oatmeal in front of her, a newspaper spread open beside it."
    "Her eyes lingered on a small article nestled in the corner of the page: '{b}Local High School Chess Club Invites New Members{/b}'. A small smile tugged at her lips, the image of a chessboard forming vividly in her mind."
    sana "Chess... I didn't even know our school had a club."  
    "Just as she murmured to herself, her dad walked in, the faint scent of tobacco still clinging to his clothes. He glanced at her curiously, noting her engrossed expression."
    show dadSprite at right
    "Dad" "{b}{color=#730348}Good morning{/color}, Sana. What are you reading with such focus?"
    sana "Oh, it's an article about our high school chess club. I didn't realize we had one. It sounds... interesting."
    "Her dad paused, setting his coffee cup down with a soft clink. His brows furrowed as he pulled out a chair and sat across from her."

    "Dad" "{b}{color=#730348}Шахматы{/color} (Chess), huh? A great game. Strategic. Demanding. But it's a {i}man's{/i} pastime, Sana. You'd need sharp instincts—an edge that girls your age don't always have."
    "Sana stiffened at his words, her fingers tightening on the edge of the newspaper. She had grown accustomed to his subtle digs, but this one cut deeper than usual."

    sana "I don't think chess cares about the gender of its players, Dad. It's about skill, practice, and strategy. Anyone can play."
    "Her dad let out a low chuckle, shaking his head."
    "Dad" "You've got a lot to learn. But hey, if it gets you to use your brain outside of school, maybe it's not a bad idea. Just don't expect much from those clubs—they're distractions, not opportunities."
    "The clock on the wall ticked steadily as Sana returned her focus to her oatmeal, biting back the urge to argue further. Her dad rose, grabbing his jacket from the back of the chair."
    "Dad" "I'll be in the study. Finish your breakfast and don't be late for school."
    
    play music "tense.mp3" fadeout 1.0 fadein 1.0 loop
    "As he turned, his wallet slipped from his pocket onto the dinner table. A crisp five-dollar bill peeked out, catching Sana's eye."
    "Her father disappeared into the next room, leaving the money unattended. Sana's mind raced. Five dollars—it wasn't much, but it was enough to buy a small treat, maybe even something for herself."

    menu:
        "Take the five-dollar bill.":
            $ persistent.took_money = True
            "Sana hesitated for a moment before slipping the bill into her pocket. A pang of guilt stirred in her chest, but she shook it off quickly."
            sana "(He won't even notice it's gone...)"
        "Leave the five-dollar bill.":
            $ persistent.took_money = False
            "Sana glanced at the bill once more before sighing softly. She pushed the newspaper aside and finished her oatmeal, leaving the money untouched."
            sana "(I'd feel awful if I took it...)"
    
    "With the decision made, Sana grabbed her bag and headed for the door, her mind swirling with thoughts of chess and her dad's cutting words. The day ahead felt heavy, but a part of her was determined to prove him wrong."
    stop music
    jump walk_to_school_1
    
    
# walk to school
label walk_to_school_1:
    scene bg_street with dissolve
    play music "soft_walk.mp3" fadeout 1.0 fadein 1.0 loop

    "The morning rain pitched down as Sana shuffled down the cracked sidewalk, clutching the crumpled $5 bill her dad handed her."
    "Her stomach growled—a sharp reminder of the meager dinner from the night before. She shook off the thought, focusing on the rhythmic crunch of her sneakers on the pavement."
    
    show joseySprite at right with fade
    Josey "Hey, Sana! Wait up!"
    "Josey jogged to catch up. She grinned, her backpack slung lazily over one shoulder."
    show sanaSprite at left with fade
    sana "Hey, Josey."
    Josey "What's with the look? You look like someone stole your lunch money... Oh wait, you don't even bring lunch half the time."
    sana "(Forced smile) Haha, very funny."

    menu:
        "Tell Josey about the $5 bill":
            sana "It's just... my dad gave me five dollars today. He never gives me cash."
            Josey "Five bucks? What are you gonna do with it? Snack bar?"
            sana "I... I don't know yet."

        "Keep it to yourself":
            sana "It's nothing. Just thinking."
            Josey "Thinking about what? Carter again? Because honestly, I think he likes you. He just sucks at showing it."
            sana "(Rolling her eyes) Carter? No, gross."

    Josey "By the way, did you hear about the chess tournament?"
    sana "What tournament?"
    Josey "Ugh, Sana. You really live under a rock sometimes. Professor Connor's been hyping it all week in chess club. Winner gets a free lunch pass for the whole week. A free week of cafeteria food, girl! Imagine that!"

    "Sana's stomach growled again, loud enough for Josey to notice. She winced, clutching her bag tighter."
    Josey "You're so in, right? You could totally win!"
    
    menu:
        "Say you'll think about it":
            sana "I don't know... I'll think about it."
            Josey "Think fast! Registration ends today."
        
        "Agree to sign up":
            sana "Yeah, I guess I could."
            Josey "That's what I'm talking about! You're gonna crush it."

    Josey "Come on, let's not be late again. "
    stop music
    jump school_recess
    
label school_recess:
    scene lunchroom with dissolve
    "Sana sat at the edge of the schoolyard, nibbling on the corner of a dry sandwich she had packed the night before. Around her, the buzz of lunchtime chatter filled the air."
    "Josey plopped down next to her, balancing a tray of fries and an apple juice box."
    show joseySprite at right with fade
    Josey "So, are you gonna sign up for the chess tournament or what?"
    show sanaSprite at left 
    sana "I said I'll think about it."

    "Before Josey could respond, the crackle of the school PA system interrupted their conversation."
    "Attention, students. This is a public announcement from Professor Connor."
    play sound "announcement_ding.mp3"
    "Are you a fan of strategy and mind games? Do you want to win a **FREE LUNCH PASS** for the whole week? Then join us in Professor Connor's classroom during lunch today for an important chess club meeting. All skill levels are welcome. See you there!"
    "The announcement ended with a loud buzz, and murmurs began to spread through the yard. Sana noticed Carter leaning against a tree, smirking in her direction."
    hide sanaSprite
    hide joseySprite
    show carterSprite at left
    carter "Hey, Sana. Heard that? Free lunch for a week. Sounds like something you'd need, huh?"
    show joseySprite at right
    Josey "Ignore him. He's just bitter because you're better than him."
    carter "(Shrugging) Sure. That's why I beat her last time."
    hide joseySprite
    show sanaSprite at right
    sana "(Annoyed) You got lucky."

    menu:
        "Decide to attend the meeting":
            sana "(Determined) I'm going. I'll show him what real luck looks like."
            Josey "That's the spirit!"

        "Hesitate and let Josey convince you":
            sana "I don't know... maybe it's not worth the trouble."
            Josey "Don't be ridiculous. You've got this, Sana. Besides, think of the free food."
            sana "(Sighs) Fine. Let's go."

    jump chess_club_announcement

label chess_club_announcement:
    scene bg_class with dissolve
    play music "piano.mp3" fadein 1.0 loop
    "Sana and Josey arrived at the classroom, finding it bustling with students. The desks had been rearranged into rows with chessboards, each one surrounded by eager faces."
    "Professor Connor stood at the front, a clipboard in hand and a smile on his face."
    show connorSprite at left
    profConnor "Welcome, everyone. It's great to see so many of you here. Today, we're kicking off the registration for the **school chess tournament**! The tournament date will be determined later."
    "The room erupted in excited murmurs."
    show joseySprite at right
    Josey "(Whispering to Sana) Looks like half the school wants that free lunch pass."
    show sanaSprite at center
    profConnor "Let me explain how this will work. The tournament will take place over the next two weeks, with matches held during lunch and after school. The winner not only earns the free lunch pass but also represents our school at the regional chess championship."
    "The murmurs grew louder, and Sana felt a mix of nerves and excitement building in her chest."
    hide connorSprite
    show carterSprite at left
    carter "(Mocking) Sounds like a lot of pressure, Sana. You sure you can handle it?"
    Josey "(Glaring) She can handle it better than you."
    carter "We'll see."

    profConnor "Now, I'll need everyone to sign up before the end of the day. If you're interested, come up to me after practice. Let's begin with some friendly matches to warm up."
    "Professor Connor gestured for the students to pair up. Sana felt Carter's gaze lingering on her."
    menu:
        "Challenge Carter directly":
            hide joseySprite
            sana "(Firmly) Let's settle this right now, Carter."
            carter "(Grinning) Bold. Alright, let's see what you've got."
            jump chess_practice_1
        "Practice with Josey first":
            hide carterSprite
            sana "I'll start with Josey. Carter can wait."
            Josey "That's what I like to hear!"
            jump chess_practice_2
    
label chess_practice_1:
    play music "chess_thinking.mp3" fadein 1.0 loop
    scene bg_chess_board with dissolve
    show carterSprite at left with fade
    "Carter tapped the board, his smug grin irritating Sana."
    carter "Ladies first."
    show sanaSprite at right
    sana "(Calmly) Don't mind if I do."
    "Sana studied the board carefully, deciding on her opening move."
    menu:
        "Play an aggressive opening":
            sana "(Confident) Let's make this quick."
            "Sana moved her pawn forward, setting up an aggressive gambit. Carter raised an eyebrow, impressed but smug."
            carter "Interesting choice."

        "Play cautiously and observe":
            sana "(Cautiously) I'll take my time."
            "Sana moved her pawn cautiously, focusing on her defense. Carter smirked, leaning back in his chair."
            carter "Playing it safe, huh? Boring."
            
    "The match continued with growing intensity, but before Sana could make her final move, Professor Connor called time."
    profConnor "Alright, everyone! That's enough for today. Make sure to sign up before you leave."
    stop music
    jump tournament_signup

label chess_practice_2:
    scene bg_chess_board with dissolve
    play music "chess_thinking.mp3" fadein 1.0 loop
    show joseySprite at left with fade
    show sanaSprite at right
    "Sana and Josey faced off, laughing as they arranged their pieces."
    Josey "Don't go easy on me, Sana. I need the practice."
    sana "Alright, but don't say I didn't warn you."
    "Sana played patiently, guiding Josey through strategies and openings. The match ended with a lighthearted checkmate."
    Josey "Ugh, you're too good. No wonder Carter's scared of you."
    sana "(Laughing) I wouldn't say scared."
    "As the practice session ended, Professor Connor called for signups."
    profConnor "Alright, everyone! That's enough for today. Make sure to sign up before you leave."
    stop music
    jump tournament_signup
        
label tournament_signup:
    scene bg_class with dissolve
    play music "hopeful_theme.mp3" fadein 1.0 loop

    "The classroom had mostly emptied, leaving Sana standing in front of Professor Connor with the signup sheet in hand."
    show connorSprite at right
    profConnor "So, have you decided?"
    show sanaSprite at left
    menu:
        "Sign up for the tournament":
            sana "(Firmly) Yes. I'm in."
            profConnor "Good choice, Sana. I'm looking forward to seeing you play."
            $ sana_signed_up = True
            jump home_scene_1

        "Decide not to sign up":
            sana "I don't think I'm ready yet."
            profConnor"That's alright, Sana. There will be other opportunities."
            jump home_scene_1
            
label home_scene_1:
    scene bg_living_room 
    play music "game_theme.mp3" fadein 1.0 loop

    "Sana sat on the worn-out couch, flipping through a school handout absentmindedly. Her dad, Mr. Volkov, entered the room, his heavy footsteps breaking the silence."
    show dadSprite at left
    "Dad" "Sana. I hear there's some kind of chess tournament at your school."
    show sanaSprite at right
    sana "(Surprised) How did you know about that?"
    "Dad" "(Grinning) I hear things. So, did you sign up?"

    if sana_signed_up:
        sana "(Firmly) Yeah, I did."
        "Dad" "(Annoyed) What? Chess is a waste of time, Sana. You have better things to focus on."
        "Dad" "(Angry) Like what? Cutting carbs and being 'thin'? You can't decide everything for me!"
        "Dad" "(Shouting) Don't take that tone with me! You should listen to your father."
        sana "(Under her breath) Maybe I'd listen if you weren't so controlling..."
        
        "The argument fizzled out as Mr. Volkov turned away, muttering under his breath. Sana stormed off to her room, her resolve to prove him wrong stronger than ever."
        stop music
        jump dad_chess_memories

    else:
        sana "(Hesitant) No... I haven't signed up yet."
        "Dad" "(Brightening up) Good. Chess is a waste of time. You shouldn't get distracted by nonsense like this."
        sana "(Frowning) What's your problem with chess, anyway?"
        "Dad" "(Avoiding eye contact) It doesn't matter. Just focus on your studies and stay on track."

        "Sana clenched her fists, feeling a wave of frustration and spite bubbling up. After her dad walked away, she sat in the quiet living room, staring at the tournament flyer. That night, she made her decision."
        call sana_typing_scene

        stop music
        jump dad_chess_memories

label sana_typing_scene:
    scene paper with dissolve
    window hide
    show screen typewriter_text("This is for me, not for him. I enjoy it anyways. Sana quietly logged into the school portal and submitted her name for the chess tournament, her heart pounding with both excitement and defiance.")
    $ renpy.pause()
    hide screen typewriter_text
    window show
    return

label sana_typing_scene_2:
    scene paper with dissolve
    window hide
    show screen typewriter_text("Carter's speed caught me off guard. But he's predictable when pressured. I need to focus on endurance and patience.")
    $ renpy.pause()
    hide screen typewriter_text
    window show
    return

# typewriting scene
screen typewriter_text(message):
    text message:
        size 52
        color "#030405"
        slow_cps 20  
        xalign 0.5
        yalign 0.5
    
        
# screen for Sana powers
screen show_powers():
    tag menu
    frame:
        background "#FFF"
        xmaximum 1000
        ymaximum 650
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        
        vbox:
            text "Sana's Powers" size 50 color "#2706bd" xalign 0.5
            spacing 15
            for power, value in sana_powers.items():
                hbox:
                    spacing 10
                    text "[power.capitalize()]: " size 30 color "#2706bd"
                    bar value value range 100 xmaximum 400 
            textbutton "Close" action Return() xalign 0.5


label dad_chess_memories: 
    scene bg_basement with dissolve
    play music "nostalgic_theme.mp3" fadein 1.0 loop
    "Later that night, Mr. Volkov descended into the dimly lit basement. He fumbled with a dusty box in the corner, pulling out a collection of old chess trophies and medals."
    "He ran his fingers over the engraving on one of the trophies"
    call screen show_trophy("Moscow Junior Chess Champion, 1956.")
    show dadSprite at left
    "Dad" "Only if things were better timed..."
    "A wistful smile played on his lips, but it quickly faded. He placed the trophy back in the box and sighed deeply."
    "As he walked back upstairs, the past felt both closer and farther away than ever before."
    
    jump morning_2
    
# screen for show trophy
screen show_trophy(engraving_text):
    modal True
    zorder 100 
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        add im.Scale("gui/trophy.png", 1100, 850) xalign 0.5 yalign 0.5
        text "[engraving_text]" size 50 color "#FFFFFF" italic True xalign 0.5 
        textbutton "Close" action Return() xalign 0.5

label morning_2:
    scene bg_bedroom with dissolve
    show screen show_powers
    play music "chess_thinking.mp3" 
    "As the morning sun rises, you realize that Sana's journey is not just about chess—it's about her abilities and how she hones them."
    "She has these powers to build on: patience, aggression, tactics, skill, memory, and confidence."
    "You'll need to make choices wisely to strengthen them."
    hide screen show_powers 
    show sanaSprite at left
    sana "Another day. Another fight, another game, another... me."
    "Her hands tightened into fists as the memories from the night before washed over her. The way they laughed. The way they thought nothing of."
    show dadSprite at right
    "Dad" "Your bus is coming in 25 minutes. Better be ready! Come east breakfast."
    "She stood and walked to the mirror, brushing a stray strand of hair behind her ear."
    sana "You're fine. You don't need anyone. You've got your books, your plans, your game. That's enough."
    "Her reflection stared back, unconvinced."
    sana "But is it? Is it really?"
    "She grabbed her school bag, slung it over her shoulder, and cast one last glance at the chessboard before leaving the room."
    sana "(Resolutely) If no one's going to fight for me, I'll fight for myself."
    "With that, she headed out the door, her heart a strange mix of determination and ache."
    jump breakfast_2

label breakfast_2:
    scene bg_diner with dissolve
    play music "game_theme.mp3" fadein 1.0 loop
    show dadSprite at left
    "Dad" "Good morning, Sana. Did you sleep well?"
    show sanaSprite at right
    sana "Yeah... I guess. You?"
    "Dad" "Fine."
    "Dad" "Sana, I wanted to talk to you about this chess tournament thing."
    sana "What about it?" 
    "Dad" "I just don't think it's a good idea. Chess is... a distraction. You should be focusing on schoolwork, not wasting time on games."
    sana "It's not just a game, Dad. You know that. You played too—don't act like it doesn't mean anything."
    menu:
        "Argue back":
            sana "I'm not giving this up. I've worked hard, and I'm going to that tournament whether you like it or not."
            "Dad" " Why are you so stubborn? I'm trying to protect you from disappointment."
            sana "Protect me? Or control me?"
        "Try to stay calm":
            sana "I'm not doing this to rebel against you, Dad. I like chess, and I want to see how far I can go."
            "Dad" "Daughter, it's not that simple. Life doesn't reward passion the way you think it will. Sometimes it's better to be practical. How are your quizzes with Professor Connor?"
    "Dad" "Besides, you don't need to prove anything to anyone. Why do you care so much about this tournament?"
    sana "Because it's the one thing I have for myself... but he wouldn't understand."
    "As Sana turned to leave, she saw her dad glance out the window, lost in thought."
    "Dad" "(Quietly, to himself) You're more like me than you think..."
    sana "(Thinking) Why does he always have to make things so complicated?"
    jump walkschool_2

label walkschool_2:
    show bg_street with dissolve
    show joseySprite at left
    Josey "So, ready for another thrilling day of high school?"
    show sanaSprite at right
    sana "Thrilling isn't the word I'd use."
    show carterSprite at center
    carter "Hey, don't forget we've got chess club after school. Big tournament's coming up."
    Josey "You two and your chess obsession. Did not know lunch pass was that deep."
    sana "It's mo.."
    carter "It's more then that."
    Josey "Well you are gonna do amazing Sana?"
    menu:
        "Express confidence":
            sana "Obviously. I've been practicing like crazy."
            Josey "That's the spirit! Just don't let it go to your head."
            carter "You'll need it on the board."
        "Downplay your chances":
            sana "I don't know. There's a lot of good players in the tournament."
            carter "Sounds about right."
            Josey "Carter, why are you here? Why? Of course. God had to curse us and make you live on our street."
            Josey "Yeah, and besides, who else am I supposed to cheer for?"
    Josey "Anyway, did you finish the history assignment?"
    sana "(Groaning) Don't remind me..."
    stop music
    
label chess_puzzle:
    play music "chess_thinking.mp3" loop
    scene bg_class with fade
    "Later in the day. At chess club practice."
    show connorSprite at left
    profConnor "So let's see who here has the mind for some puzzles!"
    profConnor "Checkmate in 1 move. Find it."
    show puzz_1 at Position(xalign=0.012, yalign=0.3)
    while True:
        menu:
            "Option 1: Knight to B6":
                $ sana_powers["skill"] += 6
                "Perfect! Checkmate."
                jump puzzle_2
            "Option 2: Queen to C8":
                $ sana_powers["skill"] -= 2
                "Not quite. Try again."
            "Option 3: Knight to C8":
                $ sana_powers["skill"] -= 2
                "Not the best move. Keep thinking!"
            "Option 4: Queen to A5":
                $ sana_powers["skill"] -= 2
                "That's not right. Try another move."
            
label puzzle_2:
    hide puzz_1
    scene bg_class
    stop music
    show connorSprite at left
    profConnor "I hope you guys found that one easy."
    show carterSprite at right
    carter "I think I could have solved that when I turned 4."
    profConnor "Very well Carter. You must have been a bright 4 year old it seems."
    carter "Uhhhhh.. yea.."
    hide connorSprite
    show joseySprite at left
    Josey "You aren't cool Carter."
    carter "Shut up. You are just here as someone's sidekick."
    Josey "How DARE.."
    hide joseySprite
    show connorSprite at left
    profConnor "HUSH. HUSH. I do not have all the day. We shall move forward with the next puzzle."
    "This one is more tactical. Solve it to ensure you gain points in tactics."
    play music "chess_thinking.mp3" loop
    show puzz_2 at Position(xalign=0.012, yalign=0.3)
    while True:
        menu:
            "Option 1: Rb8+":
                $ sana_powers["tactics"] -= 2
            "Option 2: Rxf7":
                $ sana_powers["tactics"] += 8
                "Correct! Good sight."
                jump puzzle_3
            "Option 3: Qd4":
                $ sana_powers["tactics"] -= 2
                "Not the best move. Keep thinking!"
            "Option 4: Qb4":
                $ sana_powers["tactics"] -= 4
                "That's not right. Try another move."
                
label puzzle_3:
    hide puzz_2
    scene bg_class
    show connorSprite at left
    profConnor "Okay! 5 minutes till end of the session. One last one."
    profConnor "Must say that I am rather impressed by some of you guys."
    show carterSprite at right
    carter "Can you actually make this one a challenge?"
    profConnor "Your wish granted. Now silence if you may."
    play music "chess_thinking.mp3" loop
    show puzz_3 at Position(xalign=0.012, yalign=0.3)
    while True:
        menu:
            "Option 1: Bxf7+":
                $ sana_powers["tactics"] -= 2
            "Option 2: Qxf7+":
                $ sana_powers["tactics"] += 8
                "Correct! Good sight."
                jump end_puzzles
            "Option 3: Rf1":
                $ sana_powers["tactics"] -= 2
                "Not the best move. Keep thinking!"
            "Option 4: Rd1":
                $ sana_powers["tactics"] -= 4
                "That's not right. Try another move."
      
label end_puzzles:
    hide puzz_3
    show connorSprite at left
    profConnor "Session is over. Well done all. See you soon. The tournament will be this Friday."
    show screen show_powers
    "Here is where your powers stand right now. Keep solving challenges to advance!"
    hide screen show_powers
    show carterSprite at right
    carter "You hear that guys! Only 2 days till I win the tournament. If only the stakes were higher."
    hide connorSprite
    show joseySprite at left
    Josey "You actually make me want to throw up sometimes."
    carter "How does it feel dedicating your whole lif....."
    hide joseySprite
    show sanaSprite at left
    sana "Want to play a game carter?"
    carter "UHH. umm. urm. HAHA. Are you kidding yourself?"
    sana "Oh."
    carter "I mean if you really want to."
    hide sanaSprite
    show joseySprite at left
    Josey "Seems like you are not up to it Carter."
    carter "Is it not just so lovely that you always have to interject. Annoying."
    hide joseySprite
    show sanaSprite at left
    sana "Ok. See you guys tomorrow then."
    carter "Wai... Wait. Okay. Lets play. But time is worth money. Put 5 dollars on it."
    if persistent.took_money:
        sana "(Thinks to herself) I do have five dollars... Maybe this is my chance to beat him."
        sana "Alright, Carter. Five dollars it is. Let's see if you can handle losing both the game and your money."
        hide sanaSprite
        show joseySprite at left
        Josey "That's the spirit Sana."
        carter "(Grinning) Confident, huh? Let's see how long that lasts."
        Josey "(Whispering) You've got this, Sana. Teach him a lesson."
    else:
        sana "(Thinks to herself) I don't have the money—or the time—to waste on Carter's ego."
        sana "No thanks, Carter. I do not want to gamble like that."
        carter "Backing out? It isn't gambling if I have a 110 percent chance of winning HA HA HA." 
        hide sanaSprite
        show joseySprite at left
        Josey "Actually, Carter, it just shows she's smarter than you'll ever be. Of course, you would put money on it to scare her away."
        carter "Oh, whatever! You're all so annoying. Let's just play already then!"
    "They move to the chess room. The match begins. The room falls silent as Carter and Sana focus intently on the game."
    jump sparring_with_carter
    
screen show_clock(engraving_text):
    modal True
    zorder 100 
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        add im.Scale("gui/chess_clock.png", 1100, 850) xalign 0.5 yalign 0.5
        text "[engraving_text]" size 50 color "#FFFFFF" italic True xalign 0.5 
        textbutton "Close" action Return() xalign 0.5
    
label sparring_with_carter:
    scene bg_chess_room with dissolve  
    show carterSprite at left
    carter "Alright, Sana. Ready to lose? Let me show you how a future champion plays."
    carter "U ever play with a clock you amateur?"
    show sanaSprite at right
    sana "Uhh no."
    call screen show_clock("Antique Clock 1977")
    "The experience with a clock gives Carter an internal edge."
    hide show_clock
    sana "We'll see about that, Carter."
    "The match begins. Sana carefully moves her pieces, analyzing every move Carter makes."
    sana "(Thinks to herself) He's fast. Too fast. He doesn't stop to think about his opponent/s traps."
    "Midway through the match, Sana sets up a clever trap, but Carter avoids it at the last second."
    carter "Nice try, but you're not sharp enough for me."
    sana "Maybe, but you're rushing. I've seen your endgame -- it's not as strong as you think."
    carter "Hah! Like that'll matter when you can't even get there."
    stop music
    "In the final moments, Carter wins with a quick checkmate. Sana stares at the board, analyzing what went wrong."
    sana "(Thinking) His endgame is weak. If I can just push the match longer, I can outlast him."

    $ sana_powers['confidence'] += 2
    $ sana_powers['tactics'] += 3

    show screen show_powers
    hide carterSprite
    show connorSprite at left
    profConnor "Good match, Sana. Remember, every loss is a lesson. What did you learn?"
    hide screen show_powers
    sana "That Carter isn't as unbeatable as he thinks. I must be more patient, however."
    "Night falls."
    jump night_3
    
label night_3:
    scene bg_bedroom
    play music "piano.mp3" loop
    "The room is quiet, and the soft hum of the night fills the air. Sana lies in bed, staring at the ceiling, her mind racing with thoughts of the match with Carter."
    show sanaSprite at left
    sana "(Thinking) He was fast, but reckless. I had chances to take control, but I hesitated. I need to work on my patience and tactics."
    menu:
        "Write in her diary":
            sana "Maybe putting my thoughts into words will help."
            call sana_typing_scene_2
            "Writing in her diary helps Sana organize her thoughts and feel a little calmer."
            $ sana_powers['confidence'] += 2
        "Try to sleep without writing":
            sana "No... I can't keep replaying the match in my head. I need to sleep."
            "Sana closes her eyes, but her thoughts continue to swirl, preventing her from finding peace."
            $ sana_powers['patience'] += 2

    "Despite her efforts, Sana can't sleep. Frustrated, she gets up and heads downstairs."
    stop music
    
label late_night_basement:
    scene bg_basement with fade
    play music "chess_thinking.mp3" loop
    "The dim light of the basement greets Sana as she quietly descends the stairs. To her surprise, her dad is sitting at the old wooden table, engrossed in a chess book."
    show sanaSprite at left
    sana "Dad? What are you doing down here?"
    show dadSprite at right
    "Dad" "Sana? Couldn't sleep, huh? Neither could I. But you have school tomorrow. Please sleep."
    sana "Why are you up?"
    "Dad" "It's this old book. It's full of brilliant endgame strategies."
    sana "Endgame strategies... Just what I need."
    "Dad" "What's keeping you up?"
    sana "Yeah. He's fast, but I think I can beat him if I work on my patience. I'm just... frustrated."
    "Dad" "You've been putting a lot of time into chess lately. What's driving you?"
    menu:
        "Talk about proving yourself":
            sana "It's not just about chess. I want to prove to myself—and to everyone—that I can be great at something."
            "Dad" "That's a good reason, but don't forget to enjoy the journey. Winning is just the cherry on top."
        "Talk about learning and growth":
            sana "Chess makes me think differently. It's like solving a puzzle. Every match teaches me something new."
            "Dad" "That's the right attitude. Growth is more important than winning."
    "Dad" "Alright, champ. Get some rest. You'll figure it out. But please do not lose focus of your studies. They matter much more."
    sana "I'm not giving up, no matter how hard this gets."
    "As Sana heads back upstairs, she can't help but glance back at the chess book in her dad's hands."
    jump morning_revelation
    
label morning_revelation:
    scene bg_bedroom with fade
    "The morning light streams through the curtains, and Sana rubs her eyes as she sits up in bed. Something catches her attention on the desk."
    show sanaSprite at right
    sana "The chess book from last night... Did Dad leave it here for me?"
    show bookk at Position(xalign=0.3, yalign=.3)
    "Sana picks up the book, flipping through the pages filled with diagrams and annotations. It's exactly what she needs."
    hide bookk
    "Sana has a drastic thought change. Her prior academic focused and disciplined personality would be shocked."
    play music "tense.mp3" loop
    menu:
        "Call in sick to school and study the book":
            sana "Dad is at work till 5. He would never know mhmm."
            sana "This is more important right now. I need every edge I can get for the tournament."
            "Sana spends the day deeply engrossed in the book, practicing endgame strategies and learning advanced tactics."
            $ sana_powers['skill'] += 5
            $ sana_powers['tactics'] += 5
        "Go to school and take the book along":
            sana "I'l bring it to school. I can study during breaks."
            "Sana carries the book with her, sneaking glances at it throughout the day, absorbing its lessons."
            $ sana_powers['memory'] += 3
            $ sana_powers['confidence'] += 2
    stop music
    jump evening_library
    
label evening_library:
    scene bg_library_day with dissolve
    play music "chess_thinking.mp3"
    "Sana decides to spend the afternoon at the library with Josey. The two sit across from each other, the chess book open between them."
    show joseySprite at left
    Josey "This book looks intense. 'The Complete Book of Chess Strategy'. Where did you even find this?"
    show sanaSprite at right
    sana "My dad had it. I think it's older than me. But it's packed with strategies I've never seen before."
    Josey "Well, let's see if it's helping. Play me a quick game."
    sana "You're on."
    "The two begin a practice match. Josey's style is aggressive, testing Sana's patience as she carefully plans her moves."
    menu:
        "Play defensively to frustrate Josey":
            hide joseySprite
            sana "(Thinking) *If I focus on defense, I can force her to overcommit.*"
            "Sana plays defensively, creating openings for a counterattack. Josey grows visibly frustrated, making mistakes."
            $ sana_powers['patience'] += 5
            $ sana_powers['tactics'] += 3
        "Play aggressively to match Josey's style":
            hide joseySprite
            sana "(Thinking) I'll match her aggression and see who cracks first."
            "Sana meets Josey's aggression head-on. The board becomes a battlefield, with pieces flying off as both players trade attacks."
            $ sana_powers['aggression'] += 5
            $ sana_powers['confidence'] += 3
    show joseySprite at left
    Josey "Not bad, Sana. You're really stepping up your game."
    sana "Thanks. I'm feeling more prepared for the tournament."
    "The session ends with both girls energized and ready for what's ahead."
    stop music
    jump encounter_with_carter

label encounter_with_carter:
    scene bg_street with dissolve
    play music "seventies_love.mp3" loop
    "After leaving the library, Carter appears. He's heading back home too"
    show sanaSprite at left
    sana "(Thinking) Should I talk to him? Maybe I can learn something useful."
    menu:
        "Approach Carter":
            sana "Hey, Carter. Prepping for the tournament?"
            show carterSprite at right
            carter "(Laughing) Always. Not that I need much practice. You should be the one cramming, Sana."
            sana "Confidence is great, but overconfidence... that's a different story."
            "Carter scoffs but seems slightly unnerved by Sana's calm response."
            $ sana_powers['confidence'] += 3
            hide carterSprite
        "Stay silent and observe":
            sana "(Thinking) No need to tip my hand. I'll just see what he's up to."
            "Sana watches from a distance, noticing Carter reviewing endgame strategies. She files the observation away for later use."
            $ sana_powers['memory'] += 3
    "As Sana leaves, Carter calls out to her."
    show carterSprite at right
    carter "Hey, Sana. Don't forget—Friday's the big day. Hope you're ready to lose."
    sana "We will see."
    carter "You know. I have never seen a girl have so much passion in something like chess."
    sana "Well, you are pretty sheltered."
    carter "You prove my point yet again. You speak so... god, I can't describe it. Like different. Just so unordinary."
    sana "Ok bye. If I speak to you any longer..."
    carter "Yeah yeah. See you later."
    stop music
    "The day of the tournament arrives. The nerves are there. But what more to say or do now."
    jump pre_tournament_reflection
    
label pre_tournament_reflection:
    scene bg_class with fade
    "Right before the tournament, Prof. Connor pulls Sana aside for one final pep talk."
    show connorSprite at left
    profConnor "Alright, Sana. Tomorrow's the big day. You've come a long way, but it's time to sharpen your instincts. Let's do some rapid-fire questions."
    show sanaSprite at right
    sana "Rapid-fire questions? Is this a pop quiz?"
    profConnor "(Smiling) Something like that. Trust your gut and answer quickly. Ready?"
    sana "Ready."
    play music "quizmusic.mp3" loop
    profConnor "In an open position, which is more important: bishops or knights?"
    menu:
        "Bishops":
            sana "Bishops. They thrive in open spaces with long diagonal control."
            profConnor "(Nods) Good. Keep that in mind when you see the board open up."
            $ sana_powers['skill'] += 5
        "Knights":
            sana "Knights. Their ability to jump over pieces can be a game-changer."
            profConnor "(Raises eyebrow) Interesting. You're thinking creatively. I like that."

    profConnor "What's the key focus in the opening: the center or the edges?"
    menu:
        "The center":
            sana "The center. Controlling it sets the pace of the game."
            profConnor "(Smiles) Classic chess theory. Solid answer."
            $ sana_powers['skill'] += 5
        "The edges":
            sana "The edges. Sometimes an unconventional move can surprise the opponent."
            profConnor "Not textbook, but it could throw someone off. Just use it wisely."
            $ sana_powers['skill'] -= 3

    profConnor "If you're under pressure, should you prioritize attacking or defending?"
    menu:
        "Defending":
            sana "Defending. I need to stabilize first before planning a counterattack."
            profConnor "Smart. Never attack without a strong foundation."
            $ sana_powers['patience'] += 3
        "Attacking":
            sana "Attacking. Sometimes the best defense is a good offense."
            profConnor "Bold. But it's a high-risk, high-reward choice."
            $ sana_powers['aggression'] += 4

    profConnor "If your king is exposed, should you castle early or delay?"
    menu:
        "Castle early":
            sana "Castle early. A safe king is critical in the midgame."
            profConnor "(Nods) Agreed. Don't take unnecessary risks."
            $ sana_powers['skill'] += 3
        "Delay castling":
            sana "Delay castling. Sometimes it's better to keep my options open."
            profConnor "Risky, but adaptable. I hope it works for you."
            $ sana_powers['patience'] -= 2

    profConnor "Final question. If you're ahead in material, should you trade pieces or hold your advantage?"
    menu:
        "Trade pieces":
            sana "Trade pieces. Simplifying makes it easier to convert my lead."
            profConnor "Good strategy. Keep it simple."
            $ sana_powers['skill'] += 3
        "Hold advantage":
            sana "Hold my advantage. I don't want to lose momentum by trading prematurely."
            profConnor "That's confidence. Just don't let greed trip you up."
            $ sana_powers['confidence'] += 2

    "Sana answers each question with growing confidence. Prof. Connor smiles, clearly proud of her progress."
    profConnor "You've got this, Sana. Trust your instincts and stay calm. Win or lose, make them remember you."
    sana "Thank you, Professor. I'll do my best."
    show screen show_powers
    "This is the current state of your powers!"
    stop music
    hide screen show_powers
    jump tournament_hall
    
label tournament_hall:
    scene bg_tournament with dissolve
    "The tournament hall buzzes with excitement. Players from different schools sit at tables, each focused on their boards. Sana takes her seat, her heart racing."
    show sanaSprite at left
    sana "(Thinking) Deep breaths. I've trained for this. It's just another game."
    "As the first round begins, Sana carefully studies her opponent. The match is intense, with both players trading sharp moves."
    "Sana gains the upper hand, using the strategies she practiced. She traps her opponent's queen, forcing them to resign."
    $ sana_powers['confidence'] += 5
    "Round after round, Sana pushes through, each victory fueling her resolve."
    "In the semifinal, Sana faces an aggressive player who tries to overwhelm her. She counters with patience and precision, turning their aggression into opportunities."
    $ sana_powers['patience'] += 5
    play music "nostalgic_theme.mp3" loop
    "As the final round approaches, Sana glances at the crowd—and freezes."
    show dadSprite at right
    "Her dad stands at the back of the hall, watching her with a proud yet serious expression."
    hide dadSprite
    sana "Dad... He came to watch me? But I thought he hated this. That it took away from my studies. Whyyy.. I do not get it."

    "Tears threaten to well up in Sana's eyes, but she quickly wipes them away. Her heart swells with determination."
    sana "(Thinking) I can't let him down. I'll win this for him -- NO.. for myself."

    "She closes her eyes for a moment, replaying her journey in her mind."
    sana "(Thinking) The late-night study sessions, the matches with Carter, Josey's encouragement, Prof. Connor's advice... everything has led to this."
    sana "(Thinking) No matter what happens, I'll give it everything I've got."
    
    "The final match begins. Sana's opponent is none other than Carter."
    show carterSprite at right
    carter "Ready to lose, Sana? Let's see if you've really improved."
    sana "Let's find out."
    "Sana's powers have boosted from the presence of her dad."
    stop music
    
    play music "quizmusic.mp3" loop
    "The match begins. Sana and Carter exchange a flurry of opening moves, fighting for control of the center."
    # show chess_board_start
    "Carter plays aggressively, pushing his pieces forward quickly. Sana takes her time, planning her strategy."

    menu:
        "Play defensively and wait for an opening":
            sana "I'll let him make the first mistake. Patience is key."
            $ sana_powers['patience'] += 3
            "Sana focuses on solidifying her position, carefully countering Carter's attacks."
        "Play aggressively and challenge his confidence":
            sana "Let's see how he handles the pressure."
            $ sana_powers['aggression'] += 3
            "Sana pushes her pieces forward, forcing Carter to react quickly."

    "The early game transitions into the midgame. The crowd leans forward, holding their breath with each move."

    # Choice 2: Midgame tactics
    menu:
        "Focus on controlling the center":
            sana "(Thinking) Control the center. Force him into a corner."
            $ sana_powers['tactics'] += 3
            "Sana positions her knights and bishops to dominate the center of the board."
        "Set a trap on the edges":
            sana "(Thinking) I’ll lure him into a false sense of security."
            $ sana_powers['tactics'] += 2
            $ sana_powers['memory'] += 2
            "Sana sets up a clever trap on the edge of the board. Carter takes the bait but escapes narrowly."

    "As the game enters the endgame, both players have a handful of pieces left. The tension is palpable."

    carter "You've improved, Sana. But it's not enough. I'm ending this now."
    sana "No, Carter. This is my game."

    # Choice 3: Final move
    menu:
        "Sacrifice a rook to set up a checkmate":
            sana "Sometimes you have to give up something valuable to win."
            $ sana_powers['tactics'] += 5
            "Sana sacrifices her rook, leaving Carter stunned. In three moves, she delivers checkmate!"
        "Go for a direct attack on his king":
            sana "I'll go straight for the kill."
            $ sana_powers['confidence'] += 3
            "Sana attacks aggressively, forcing Carter into a losing position. He resigns!"

    # Outcome
    if sana_powers['confidence'] + sana_powers['tactics'] > 25:
        "Carter slams his hand on the table as the crowd erupts in cheers. Sana has won the tournament!"
        sana "(Thinking) I did it. I actually did it!"
        carter "Congrats. You earned it."
        sana "I'll be ready, Carter. Anytime."
    else:
        "Carter delivers a swift checkmate. Sana sits back, disappointed but determined."
        sana "(Thinking) I lost... but I'll learn from this. Next time, I'll beat him."
        profConnor "(From the audience) Good job, Sana. You fought well."
        $ sana_powers['confidence'] += 3

    jump tournament_aftermath
    

label tournament_aftermath:
    scene bg_tournament with dissolve
    "The tournament hall slowly empties as players and spectators head home. Sana lingers, staring at the trophy in her hands."
    show sanaSprite at center
    sana "(Thinking) I did it... but this is just the beginning. Winning here doesn't mean I've mastered the game."
    "Prof. Connor approaches her with a smile."
    show connorSprite at left
    profConnor "Well done, Sana. You earned every bit of this victory. But if you're serious about climbing the ranks, the puzzles and matches ahead will be even harder."
    sana "I know. I want to keep improving. How do I start?"
    profConnor "The next step is solving advanced puzzles daily. I'll share some resources with you. And you’ll need to find more skilled opponents to challenge yourself."
    sana "Got it. Thanks for believing in me, Prof. Connor."
    profConnor "It's not about me believing in you, Sana. It's about you believing in yourself. Keep climbing."
    "As he walks away, Sana looks down at her trophy, determination blazing in her eyes."
    jump letter_to_mom


label sana_typing_scene_3:
    scene paper with dissolve
    window hide
    show screen typewriter_text("Dear Mom, I wanted to tell you about something important to me. Today, I won my first chess tournament. It wasn’t easy, but I’ve been working really hard. I know you’ve always worried about me balancing my studies and hobbies, but chess has become more than a game to me. It's taught me patience, strategy, and how to keep going even when things get tough...")
    $ renpy.pause()
    hide screen typewriter_text
    window show
    return

label letter_to_mom:
    play music "nostalgic_theme.mp3" loop
    scene bg_bedroom with dissolve
    "That evening, Sana sits at her desk, staring at a blank sheet of paper. The dim glow of her desk lamp bathes the room in a soft light."
    show sanaSprite at left
    sana "Mom always wanted me to focus on my studies, but maybe... maybe she'd understand if I tell her why this means so much to me."
    "She begins writing."
    call sana_typing_scene_3
    "Satisfied with her letter, she seals it in an envelope and sets it aside for mailing."
    jump first_advanced_puzzle

label first_advanced_puzzle:
    scene bg_library_day with dissolve
    "The next morning, Sana finds herself back at the library, flipping through a book of advanced chess puzzles."
    sana "These are brutal. But if I want to compete at the next level, I have to get through this."
    "The book is open to a particularly difficult puzzle. Sana stares at the board, trying to find the winning sequence."
    menu:
        "Sacrifice the queen to set up a checkmate":
            sana "(Thinking) Sacrificing the queen seems counterintuitive, but it could lead to a forced checkmate."
            $ sana_powers['tactics'] += 5
            "Sana moves the queen in her mind, visualizing the opponent's response. After three moves, she sees the checkmate."
            sana "Yes! Got it."
        "Focus on defensive play to trap the king":
            sana "(Thinking) If I defend my pieces and control the board, I might be able to trap the king."
            $ sana_powers['patience'] += 5
            "Sana repositions her pieces, creating a wall of defense. She sees how the opponent is cornered after five moves."
            sana "This works too. Different paths, same result."
    "She marks the puzzle as solved, feeling a surge of confidence."
    sana "One down, hundreds to go."
    jump sana_and_carter
    
default sana_emotion_carter = 0  # Neutral starting point
    
label sana_and_carter:
    scene bg_park_bench with dissolve
    play music "seventies_love.mp3" loop
    "Sana sits on a park bench, staring at a chessboard on her lap. Carter walks over and plops down beside her without asking."
    show carterSprite at right
    carter "You always come here when you're in your head. What's up?"
    show sanaSprite at left
    menu:
        "Tell Carter the truth":
            $ sana_emotion_carter += 1  # Increases her positive feelings
            sana "I just... feel like I'm not ready. What if I embarrass myself?"
            carter "Embarrass yourself? Sana, you're better than half those players already. Just play your game."

        "Brush him off":
            $ sana_emotion_carter -= 1  # Decreases her positive feelings
            sana "Nothing. You wouldn't get it."
            carter "Oh, please. You're not fooling me. It's about chess again, isn't it?"

    "Sana sighs, moving a pawn absently on the board."
    sana "It's not just about the tournament. My parents... I feel like I'm fighting for their approval. Like if I fail, I’ll let everyone down."

    menu:
        "Agree with Carter's advice":
            $ sana_emotion_carter += 1
            sana "He's annoying, but he's right. I can't lose sight of why I started this."
            carter "See? Now you're getting it. You've got this, Sana."

        "Push back on his advice":
            $ sana_emotion_carter -= 1
            sana "That's easy for you to say. You don't understand what it's like to have this kind of pressure."
            carter "Maybe not, but you're overthinking this. Just focus on your game."

    "Carter stands, brushing off his jeans."
    carter "Come on. I'll give you a practice match. Just don't cry when I win."

    if sana_emotion_carter >= 2:
        sana "You wish. But thanks for the pep talk. I needed it."
    elif sana_emotion_carter <= -2:
        sana "You're so cocky. Let's just get this over with."
    else:
        sana "Sure. Let's play."
    jump mom_backstory
    
    
# cutscene images
image mouma = im.Scale("mom_visionary.jpg", 1920, 1080)
image rainy = im.Scale("rainy_seventies.webp", 1920, 1080)
image mouma_preach = im.Scale("mouma_talking.jpg", 1920, 1080)
image poor_health = im.Scale("seventies_hospital.jpg", 1920, 1080)
image chess_worn = im.Scale("worn_set.webp", 1920, 1080)
image mouma_final = im.Scale("mouma_final.jpg", 1920, 1080)
image political = im.Scale("tension_political.avif", 1920, 1080)
label mom_backstory:
    scene bg_living_room with dissolve
    play music "nostalgic_theme.mp3" loop
    "So why this sudden or maybe always existing interest in Chess? Why Sana?"
    window hide
    pause(1)
    scene black with fade
    pause(1)
    window show
    # cut scene starts
    "When Sana was little, chess wasn't just a game. It was a bond—a language she shared with her mother."
    pause(2)
    scene mouma
    "Her mother, Aisha, wasn't just a player; she was a visionary. A quiet force on the chessboard, and a fierce advocate for thinking five steps ahead in life."
    with dissolve
    pause(2)
    scene rainy
    "Sana remembered rainy afternoons by the window, with the rhythmic tap of raindrops blending into the sound of chess pieces clicking on the board."
    pause(3) 
    scene mouma_preach
    "“Think beyond the move in front of you,” her mother would say. “See the whole board, Sana. Life is no different.”"
    with dissolve
    pause(3)
    scene poor_health
    "But life wasn't as predictable as chess. When Sana was ten, her mother's health started to decline. A persistent cough turned into days spent in the hospital. Not only that, she chose a different route with Russian politics."
    pause(3)
    "Her mother's once-strong hands, so steady on the chessboard, grew weak. Yet, even then, she taught Sana. Not just moves, but lessons on resilience."
    pause(3)
    scene chess_worn
    "One evening, Aisha handed Sana her most treasured possession: a worn chess set. The same one they had used since Sana could barely reach the table."
    pause(3)
    scene mouma_final
    "“Promise me, Sana,” she said with a smile that didn't quite reach her tired eyes. “Promise me you'll keep playing, no matter what. Even when it gets hard.”"
    pause(3)
    scene political
    "Sana promised. And for years, she kept that promise. With that, her dad relocated them to the US because of the stability and political tension arising from Aisha's political involvement."
    pause(2)

    # Transition back to present
    scene bg_living_room with dissolve
    show sanaSprite at left
    "As Sana sat across from her dad in the dimly lit room, she realized how far she'd come since those rainy afternoons." 
    sana "(Thinking) Maybe... Maybe chess isn't just about winning. It's about remembering her. About honoring what she taught me."
    pause(2)

    show dadSprite at right
    "Dad" "Sana, I'm proud of you. Your mother.. I do not wish to indulge in further conversation about."
    sana "Thanks, Dad."
    jump time_skip
    
image fast = im.Scale("fastForward.jpg", 1920, 1080)
    
label time_skip:
    scene fast with dissolve
    play music "timeChange.mp3" loop
    "Sana has grown more confident, balancing her chess passion with schoolwork. But today, a tough science test awaits her."
    "Let's see how your story pans out!"
    $ sana_powers["skill"] += 45
    $ sana_powers["patience"] += 45
    $ sana_powers["aggression"] += 45
    $ sana_powers["memory"] += 45
    $ sana_powers["tactics"] += 45
    $ sana_powers["confidence"] += 45
    
    jump science_test

label science_test:
    play music "quizmusic.mp3" loop
    scene bg_class with dissolve
    show connorSprite at right
    profConnor "Alright, Sana. It's time for the test. Answer carefully."
    
    $ test_score = 0
    "What is the atomic number of Carbon?"
    menu:
        "6":
            $ test_score += 1
            sana "6!"
            profConnor "Correct."
        "12":
            sana "12?"
            profConnor "Incorrect. It's 6."  
    "Which planet is known as the Red Planet?"      
    menu:
        "Mars":
            $ test_score += 1
            sana "Mars."
            profConnor "Good job!"
        "Venus":
            sana "Venus?"
            profConnor "No, it's Mars."
    # Question 3
    "What is H2O commonly known as?"
    menu:
        "Water":
            $ test_score += 1
            sana "Water."
            profConnor "That's correct."
        "Oxygen":
            sana "Oxygen?"
            profConnor "No, it's water."

    profConnor "Alright, let's see how you did..."
    if test_score == 3:
        profConnor "Perfect score! 3/3. Excellent work, Sana."
    elif test_score == 2:
        profConnor "Not bad! 2/3. You did well."
    else:
        profConnor "1/3 or less. You'll need to study harder next time."
    jump dad_grilling

label dad_grilling:
    scene bg_living_room with dissolve
    show dadSprite at right
    show sanaSprite at left
    play music "tense.mp3"
    "Dad" "Sana, I saw your grades were supposed to drop today. Did you get your report card?"
    menu:
        "Tell the truth":
            sana "Yeah, I did . To say the least"
            "Dad" "Alright. Show it to me."
            show screen report_card
            "Dad" "This is beyond disappointing. We'll talk more about this at the parent-teacher meeting tomorrow. For now, get ready for school."
            hide screen report_card
            jump parent_teacher_meeting
        "Lie":
            sana "No, I haven't received it yet."
            "Dad" "Hmm... Are you sure? That's strange."
            jump dad_finds_out
            
screen show_bagpack(engraving_text):
    modal True
    zorder 100 
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        add im.Scale("gui/sanaBagpack.png", 1100, 850) xalign 0.5 yalign 0.5
        text "[engraving_text]" size 50 color "#FFFFFF" italic True xalign 0.5 
        textbutton "Look Further" action Return() xalign 0.5
        
screen report_card():
    frame:
        xalign 0.5 
        yalign 0.3
        vbox:
            spacing 10   
            text "Student Report Card" size 40 style "default" xalign 0.5
            text "Name: Sana" size 30
            text "Class: 10th Grade" size 30    
            text "Subjects and Grades:" size 35 style "default" bold True   
            hbox:
                spacing 20   
                vbox:
                    text "Math" size 28
                    text "Science" size 28
                    text "English" size 28
                    text "History" size 28
                    text "Physical Education" size 28
                    text "Art" size 28 
                vbox:
                    text "C-" size 28 color "#FF5555"
                    text "D" size 28 color "#FF5555"
                    text "C" size 28 color "#FF5555"
                    text "D+" size 28 color "#FF5555"
                    text "C-" size 28 color "#FF5555"
                    text "C+" size 28 color "#FF5555"       
            text "Teacher's Note:" size 35 style "default" bold True
            text "Sana is a bright student but seriously needs to work on consistency and focus." size 28 italic True

label dad_finds_out:
    play music "chess_thinking.mp3" loop
    scene bg_living_room with dissolve
    show dadSprite at right
    show sanaSprite at left
    "It's late in the evening, and Sana is sitting at the dinner table with her dad. The air feels tense, her dad unusually quiet."
    "Dad" "Sana, are you sure there's nothing you want to tell me? About school?"
    sana "No, Dad. Everything's fine. I told you already, we haven't gotten our report cards yet."
    "Dad" "Hmm. Alright, then."
    "Sana forces a smile, feeling her pulse quicken as she excuses herself from the table."
    sana "Goodnight, Dad. I'm going to bed early. Busy day tomorrow."
    "Dad" "Goodnight."
    "Sana retreats to her room, relieved but uneasy. She climbs into bed, trying to shake the feeling of guilt gnawing at her."

    scene bg_bedroom with dissolve
    "Hours later, the house is dark and quiet. The sound of a clock ticking fills the room as Sana tosses and turns in bed."
    show sanaSprite at left
    sana "Did I really fool him? Ugh, this is so stressful... Maybe I should've just told the truth. But I can't disappoint him like that."
    "Meanwhile, in the living room, her dad is sitting on the couch, deep in thought."
    scene bg_living_room with dissolve
    show dadSprite at right
    "Dad" "Something's not adding up. Sana's been acting strange lately. And that excuse... it didn't sit right with me."
    "His gaze shifts toward Sana's school bag, half-hidden under the coffee table where she left it earlier."
    stop music
    play music "tense.mp3"
    "Dad" "I shouldn't invade her privacy, but if she's hiding something important, I need to know."
    "Carefully, he pulls the bag from under the table, opening it quietly so as not to wake Sana. His heart sinks as he finds an envelope marked with the school's logo."

    show screen show_bagpack("Sana's Bagpack")
    "Dad" "She lied to me."
    hide screen show_bagpack
    show screen report_card
    "He flips open the report card and scans the grades. His jaw tightens."
    hide screen report_card
    "Dad" "She didn't do well, and she lied about this! Doesn't she trust me?"
    stop music
    scene bg_porch with fade
    show dadSprite at right
    show sanaSprite at left
    
    play music "chess_thinking.mp3"
    "The next morning, Sana walks into the living room to find her dad holding the report card. Her heart drops."
    "Dad" "Sana, we need to talk."
    sana "Dad, I—"
    "Dad" "I found this in your bag last night."
    "He holds up the report card. Sana freezes."
    sana "Oh uh.."
    "Dad" "Why did you lie to me, Sana? I thought we had a better relationship than this."
    menu:
        "Apologize sincerely":
            sana "I'm sorry, Dad. I just... I didn't want you to be disappointed in me. I thought if I could fix it before you found out—"
            "Dad" "Disappointed? Sana, what disappoints me is dishonesty, not low grades. We all make mistakes, but we can't grow from them if we hide from the truth."
            sana "I understand."
        "Argue defensively":
            sana "Maybe if you didn't pressure me so much, I wouldn't have to hide things from you!"
            "Dad" "Pressure? Sana, this is about trust. I push you because I know what you're capable of. But lying doesn't solve anything."
            sana "You just don't get it."

    "After a long silence, Sana lowers her head, guilt and frustration warring inside her."
    "Dad" "We'll talk more about this at the parent-teacher meeting tomorrow. For now, get ready for school."

    jump parent_teacher_meeting

label parent_teacher_meeting:
    stop music
    scene bg_class with fade
    show sanaSprite at center
    show dadSprite at left
    show connorSprite at right
    profConnor "Sana, your father and I have been discussing your recent academic performance."
    "Dad" "Sana, I'm very disappointed in you. How could you keep this from us?"
    sana "I'm sorry, Dad. I was just trying to-"
    "Dad" "Trying to what? Lie to us? That's not how I raised you."
    play music "tense.mp3" loop
    menu:
        "Defend myself":
            sana "Maybe if you didn't put so much pressure on me, I wouldn't have felt the need to hide things!"
            "Dad" "This isn't about pressure, Sana. It's about trust. I push you because I know what you're capable of."
            profConnor "Your father is right, Sana. Lying doesn't solve anything."
        "Apologize sincerely":
            sana "I'm sorry, Dad. I just... I didn't want you to be disappointed in me."
            "Dad" "Disappointed? Sana, what disappoints me is dishonesty, not low grades. We all make mistakes, but we can't grow from them if we hide from the truth."
            sana "I understand."
    
    profConnor "Sana, I have an idea. What if you focused solely on your chess passion? I believe you have the potential to make a real impact."
    "Dad" "Chess? Sana, you can't be serious. That's not a real career path."
    sana "But Dad, maybe Professor Connor is right. I love chess, and I could-"
    "Dad" "No, Sana. I did not raise you to be so rash. You will finish your schooling, and that's final."
    
    "Dad storms out, leaving Sana and Professor Connor alone."
    hide dadSprite
    profConnor "Sana, you have a chance to change things for young girls all around. Don't let this opportunity slip away."
    sana "But what about dad? He would never agree."
    profConnor "All the cards add up Sana. Chess is in your blood. You are from a chess playing lineage. Do not let your father's disappointments prevent you"
    jump school_lunch_4
    
label school_lunch_4:
    play music "nostalgic_theme.mp3" loop
    scene lunchroom with fade
    show sanaSprite at right
    show joseySprite at left
    sana "Hey, Josie. Did you hear the new song by that band we like?"
    Josey "Oh, yeah! It's so good. I can't stop listening to it. Have you checked out their new music video?"

    menu:
        "Discuss the music video":
            sana "No, I haven't! What did you think of it?"
            Josey "It's really creative, right? I loved the visual effects they used."
            sana "Same, it really fits the vibe of the song perfectly."
        "Talk about a different hobby":
            sana "No, but I've been meaning to. Have you been keeping up with that new TV show we were talking about?"
            Josey "Oh, yes! I'm totally hooked. Did you see the latest episode?"
            sana "No, not yet. Was it any good?"
            Josey "It was so good! There was this crazy plot twist that I didn't see coming at all."
            sana "Oh man, now I can't wait to watch it. We'll have to discuss it later."
        "Compliment Josie":
            sana "No, but I've been meaning to. You know, Josie, I really admire how passionate you are about music."
            Josey "Aw, thanks Sana. Music has always been such a big part of my life. I'm glad we share that in common."
            sana "Me too. It's nice to have someone who really understands that."
    sana "Josey, I just wanted to say thank you. For always being there for me, no matter what."
    Josey "Of course, Sana. What are friends for? But why the sudden thanks?"
    
    sana "Well, it's just... a lot has been happening, and I wanted you to know how much I appreciate your support."
    
    Josey "Sana, what's going on? You can talk to me, you know that, right?"
    
    sana "I'll tell you another time. For now, let's just enjoy our last lunch, okay?"
    Josey "Last??? What do you mean by that?"
    sana "When I win it for us all, for all young girls in the world, it will have then been worth it."
    Josey "Sana, but that is so unrealistic. I am going to miss you"
    sana "I know and I will always have you in my heart. But please keep supporting me."
    Josey "Okay, Sana. I'm here for you, always."
    stop music
    
    jump carter_confrontation
    
label carter_confrontation:
    play music "seventies_love.mp3" loop
    scene exiting_school with fade
    show carterSprite at left
    show sanaSprite at right
    carter "Sana! Hey, I heard about what happened. Are you really going to drop out?"
    if sana_emotion_carter <= 3:
        menu:
            "Brush him off":
                sana "Why do you even care, Carter? We haven't been friends for a long time."
                carter "I... I guess I don't. I just thought, you know, we used to be close."
                sana "Well, things change. Now if you'll excuse me, I have more important things to worry about."
                carter "Sana, wait! I'm sorry, I know I've been a jerk to you in the past."
                sana "Sorry doesn't change anything, Carter. I need to focus on my chess now."
                jump dinner_conversation
            "Engage honestly":
                sana "Yes, Carter, it's true. I'm considering focusing on my chess."
                carter "Sana, I... I'm sorry. My hatred for you, it was just jealousy and immaturity. I never should have treated you that way."
                sana "I appreciate your honesty, Carter, but I'm not sure I can forgive you so easily. You really hurt me."
                carter "I understand. I just wanted you to know that I support your decision, even if we're not friends anymore."
                sana "Thank you, Carter. That means a lot to me."
                jump dinner_conversation
    else:
        sana "Yes, Carter, it's true. I'm considering focusing on my chess."
        carter "Sana, I... I'm so sorry. My hatred for you, it was just jealousy and immaturity. I never should have treated you that way."
        sana "Carter, I... I know. I can see that now." 
        carter "Sana, I want you to know that I support you, no matter what you decide. You're an amazing player, and you deserve to chase your dreams."
        sana "Thank you, Carter. That means a lot to me." 
        menu:
            "Open up to him":
                sana "You know, Carter, I've really missed our friendship. I was always so afraid to let you back in, but I think I'm ready to try again."
                carter "Sana, I... I don't know what to say. I'm honored that you're willing to give me another chance."
                sana "Just promise me you'll be there for me, even if things get tough."
                carter "I promise, Sana. I'll be by your side, no matter what."
                $ sana_emotion_carter += 4
                jump dinner_conversation
            "Remain cautious":
                sana "I appreciate your honesty, Carter, but I'm not sure I'm ready to trust you again just yet."
                carter "I understand, Sana. I know I have a lot of work to do to earn back your trust. But I want you to know that I'm here for you, whenever you're ready."
                sana "Thank you, Carter. I'll keep that in mind."
                jump dinner_conversation
    jump dinner_conversation

label dinner_conversation:
    scene bg_diner with fade
    show dadSprite at left
    show sanaSprite at right
    play music "heroMusic.mp3" loop
    "The dinner table is silent as Sana and her father sit across from each other."
    "Dad" "So, you've made your choice."
    sana "Dad, I-"
    "Dad" "You must do everything in your power to succeed. Anything less is unacceptable."
    sana "I will, Dad. I promise."
    "Dad" "Good. You remind me so much of your mother."
    "Sana is taken aback by her father's words, unsure of what to make of the cryptic statement."
    "Practice must commence."
    jump library_puzzles
    
    
image puzz_4 = im.Scale("puzzle4.jpg", 400, 400)
image puzz_5 = im.Scale("puzzle_5.jpg", 400, 400)
image puzz_6 = im.Scale("puzzle6.webp", 400, 400)
    
label library_puzzles:
    scene bg_library_day with fade
    play music "chess_thinking.mp3" loop
    "Sana finds herself in the quiet solace of the school library, determined to focus on her chess."
    "She sits down at a table and pulls out a set of advanced chess puzzles, determined to hone her skills."
    show puzz_4 at Position(xalign=0.012, yalign=0.3)
    while True:
        menu:
            "Option 1: Knight captures f7":
                $ sana_powers["skill"] -= 1
                "Wrong!"
            "Option 2: Queen to C8":
                $ sana_powers["skill"] -= 1
                "Not quite. Try again."
            "Option 3: Pawn to e6":
                $ sana_powers["skill"] -= 1
                "Not the best move. Keep thinking!"
            "Option 4: Queen to G6":
                $ sana_powers["skill"] += 8
                "Awesome work."
                jump puzzle_5
    
label puzzle_5:
    hide puzzle_4
    sana "Okay! I need to be able to solve middlegame puzzles where the easiest solution is not apparent."
    $ sana_powers['patience'] += 5
    show puzz_5 at Position(xalign=0.012, yalign=0.3)
    while True:
        menu:
            "Option 1: Qg8+":
                $ sana_powers["skill"] += 12
                "Perfect!"
                jump puzzle_6
            "Option 2: Ng8+":
                $ sana_powers["skill"] -= 2
                "Close! Maybe there is a move before you plat this."
            "Option 3: Bxf7":
                $ sana_powers["skill"] -= 2
                "Not the best move. Keep thinking!"
            "Option 4: Qh8+":
                $ sana_powers["skill"] -= 2
                "That's not right. Try another move."
                    
label puzzle_6:
    hide puzz_5
    sana "Ok! Last one for today."
    show puzz_6 at Position(xalign=0.012, yalign=0.3)
    while True:
        menu:
            "Option 1: Bxf6":
                $ sana_powers["skill"] -= 1
                "TO your dismay. This is wrong."
            "Option 2: Rxf6":
                $ sana_powers["skill"] -= 2
                "Not quite. Try again."
            "Option 3: Nh5":
                $ sana_powers["skill"] -= 2
                "Not the best move. Keep thinking!"
            "Option 4: Qg5":
                $ sana_powers["skill"] += 10
                "Amazing! A stunning sacrifice."
                show screen show_powers
                "This is where you now stand!"
                hide screen show_powers
                jump chess_circuit
    
image bg_circuit = im.Scale("chess_circuit_image.jpg", 1920, 1080)                
                    
label chess_circuit:
    play music "chess_thinking.mp3" loop
    scene bg_circuit with dissolve
    "Time passes and Sana plays more and more."
    "She has come to a point where she is confident in her abilities."
    "Carter tells Sana about these underground chess tournaments going on in the town. They decide to go to one together."
    "Carter coming along with you has really made your confidence go up."
    $ sana_powers['confidence'] += 10
    show sanaSprite at center
    show carterSprite at left
    sana "This place... it's kind of intimidating. Are you sure about this, Carter?"
    carter "Come on, Sana. You're going to crush it here. Look at these guys—half of them probably can’t even spell Sicilian Defense."
    sana "That's oddly specific, Carter."
    carter "Hey, I'm just saying. You've got this. Plus, I'm here for moral support. And snacks."
    sana "Thanks. Really, I appreciate it."

    "They walk deeper into the dimly lit room, where chessboards are scattered across small tables. The smell of coffee and faint cigarette smoke lingers in the air. An older man with a thick Russian accent steps forward."
    show anatolySprite at right
    Anatoly "You are here to play, da? You think you can handle the heat, little one?"
    sana "I didn’t come here to watch."
    carter "Whoa, alright! Somebody brought their game face."
    Anatoly "Ha! Confident. Good. Sit, and we shall see if it is more than talk."

    "Sana takes her seat across from Anatoly. Carter stands behind her, fidgeting with his bag of chips. The room grows quiet as the game begins."

    menu:
        "Rely on your instinct and play confidently.":
            sana "Alright, let’s do this."
            "Sana begins the game with an aggressive opening, throwing Anatoly off balance. She presses her advantage, maintaining strong momentum throughout the match."  
            Anatoly "Not bad... but let us see how you handle pressure."
            "Despite Anatoly’s best efforts to recover, Sana remains in control and eventually claims victory."
            sana "Thanks for the game. But maybe next time, don’t underestimate me."
            Anatoly "Hmph. Confidence is good. Let us hope it is not just luck."

        "Use Sana's past 'powers' to predict Anatoly's strategy.":
            show screen show_powers
            sana "(Okay, think. His style is probably defensive but aggressive when provoked. I need to bait him into overextending.)"
            hide screen show_powers
            $ chosen_skill = renpy.input("Type a skill to boost: 'Prediction', 'Focus', or 'Reading Opponents'").strip().lower()
            "Sana carefully observes Anatoly’s moves, predicting his patterns based on her previous study of defensive players."
            carter "Oh man, she’s in the zone. I don’t think she’s even blinking."
            "When Anatoly sets up a trap, Sana anticipates it and counters flawlessly, surprising him."
            Anatoly "You knew what I was doing before I did. How is this possible?"
            sana "A good chess player knows the board. A great one knows their opponent."

        "Play conservatively and wait for an opportunity.":
            sana "Let's see how this unfolds."
            "Sana takes a defensive approach, cautiously responding to Anatoly's moves. The game drags on, with both players trying to outlast the other."
            carter "You've got this, Sana. Just hang in there!"
            "Finally, Anatoly makes a mistake under pressure, and Sana capitalizes on it, securing the win."
            Anatoly "A slow but effective strategy. You have patience, little one. That is rare."
    "After the game, Anatoly steps forward and extends his hand."
    Anatoly "You have skill, girl. But skill alone will not carry you. We shall see if you have what it takes to rise further."
    carter "That. Was. Amazing! You totally destroyed him!"
    sana "It's just one match, Carter. But yeah, it felt... good."
    "Chatter spreads around town. The newspaper titles are rather misogynistic though. People are in disbelief a mere teenage girl could accomplish this."
    jump media_spotlight
    
image media_with_sana = im.Scale("media_sanaa.jpg", 1920, 1080)

screen show_newspaper(engraving_text):
    modal True
    zorder 100 
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        add im.Scale("gui/newspaperr.webp", 700, 500) xalign 0.5 yalign 0.5
        text "[engraving_text]" size 50 color "#FFFFFF" italic True xalign 0.5 
        textbutton "Close" action Return() xalign 0.5
    
label media_spotlight:
    scene media_with_sana with fade
    play music "heroMusic.mp3" loop
    "A few weeks after her underground victory, Sana receives unexpected attention."
    "A local journalist, intrigued by her rapid rise, reaches out for an interview."
    show sanaSprite at right
    "Sana Malik, the ‘Wild Queen’ of the underground chess scene—how does it feel to have a nickname like that?"
    sana "‘Wild Queen?’ Really? I didn't agree to that name."
    "It's catchy, though, don't you think? Your bold, unpredictable style on the board has people talking. What drives you?"
    sana "It's not about being bold. It's about seeing opportunities where others see walls. Chess is my way of proving that I belong."
    "And your family? How do they feel about your rise?"
    sana "They... have mixed feelings. My dad doesn't exactly see this as a career path."
    "Interesting. A rebel on and off the board, then. That'll make for a great story."

    "The next day, the article is published, and Sana's face is plastered on the front page of the local newspaper."
    show screen show_newspaper("‘The Wild Queen Takes the Underground by Storm.’")
    show carterSprite at left
    sana "‘Wild Queen.’ Ugh, that name is going to stick, isn’t it?"
    hide screen show_newspaper
    carter "It's better than something like ‘Pawn Princess.’ Embrace it, Sana."
    play music "iphone-sound.mp3" loop
    "Her phone buzzes. It's her father."
    sana "Hello?"
    stop music
    "Dad" "Sana. I saw the article."
    sana "Oh. What did you think?"
    "Dad" "I think this is all getting out of hand. You're making a spectacle of yourself."
    sana "A spectacle? Dad, I'm winning. Isn't that what matters?"
    "Dad" "Winning what, Sana? Respect? Fame? None of this is going to give you a real future. It's time to think about your priorities."
    "The call ends abruptly, leaving Sana with a knot in her stomach."

    carter "Hey. You okay?"
    sana "Yeah. Just... family stuff."
    carter "Well, for what it's worth, I think you're doing amazing. And that ‘Wild Queen’ thing? Totally suits you."
    $ sana_emotion_carter += 4
    sana "Thanks, Carter. That means a lot."

    jump evening_dad_2
    
label evening_dad_2:
    scene bg_living_room with fade
    play music "timeChange.mp3"
    "The evening is quiet except for the sound of a ticking clock. Sana is seated on the couch, scrolling through her phone when her dad walks in with a folder in hand."
    show dadSprite at left
    show sanaSprite at right
    "Dad" "Sana, I need to talk to you."
    sana "What is it, Dad?"

    "Her dad sits down across from her, placing the folder on the coffee table between them."
    stop music
    "Dad" "This came in today. A sponsorship offer from a major corporation. They're willing to support your chess journey." 
    show screen offer_letter
    sana "What's this?"
    "Dad" "Take a look for yourself. It's everything I've ever wanted—financial stability, travel expenses, and a stipend."

    menu:
        "Read the letter.":
            hide screen offer_letter
            sana "A yearly stipend... Full travel and accommodation support..."
            sana "Wait, what's this about scripted public appearances and wearing their logo everywhere?"

        "Push the letter aside.":
            hide screen offer_letter
            sana "I don't need to read this. I already know what it is—another way to put me in a box." 

    "Dad" "This isn't just about you, Sana. This is about your future. You need stability, not dreams."
    sana "Stability? By selling out my passion? By turning into a walking advertisement?"
    "Dad" "You can't afford to be picky! Chess doesn't pay the bills. Do you think I can keep supporting you forever?"
    sana "I don't want your support if it means giving up who I am. I won't trade my passion for a paycheck."

    "Her dad slams the folder shut, his frustration evident."
    play music "tense.mp3" loop
    "Dad" "You've always been so stubborn. You think you know better than everyone else. Fine! If you want to ruin your life, go ahead. But not under my roof."
    sana "What? Are you serious?"
    "Dad" "Yes, Sana. If you're not going to listen, then it's time for you to leave."
    "The weight of his words hangs in the air. Sana's heart sinks, but she straightens up, refusing to let her emotions show."
    sana "Fine. I'll go."
    "Without another word, she storms out of the room, heading to pack her things."
    stop music
    jump stay_at_carters

screen offer_letter():
    frame:
        xalign 0.5
        yalign 0.5
        background "#f0f0f0"
        padding (20, 20)
        vbox:
            spacing 20
            text "Sponsorship Offer Letter" size 40 style "default" color "#582999" bold True
            text "Company: Global Chess Ventures" size 36 color "#000000" bold True
            text "Stipend: $50000 a year" size 32 color "#000000"
            text "Conditions:" size 32 color "#582999" bold True
            vbox:
                spacing 10
                text "1. Full travel and accommodation coverage." size 32 color "#000000"
                text "2. Mandatory public appearances as per schedule." size 32 color "#582999"
                text "3. Wearing the company logo during all matches." size 32 color "#000000"
                text "4. Adherence to a scripted public persona." size 32 color "#582999"

image carters_living_room = im.Scale("carter_living.jpg", 1920, 1080)
image airplane_interior = im.Scale("airplane_russia.jpg", 1920, 1080)

label stay_at_carters:
    scene carters_living_room with dissolve
    play music "seventies_love.mp3" loop
    "Sana sits on Carter's worn-out couch, surrounded by his books and chess memorabilia."
    show carterSprite at right
    carter "You know, my couch isn't exactly five-star, but it's got character."
    show sanaSprite at left
    sana "I've slept on worse. Trust me."
    carter "So, does this mean I finally have a chess champion as a roommate? Should I prepare for paparazzi at the door?"
    sana "You wish. I'm just trying not to overstay my welcome."
    carter "Sana, if anyone is doing me a favor, it's you. Besides, it's nice having someone around who doesn't mind my bad coffee and worse jokes."
    sana "Your jokes, definitely. The coffee? Jury's still out."
    carter "Speaking of, maybe I should make you breakfast tomorrow. Pancakes, perhaps?"
    sana "Flirting via pancakes. Bold move."
    carter "Hey, I'm a man of many talents. Chess and culinary arts are just the start."
    $ sana_emotion_carter += 5
    "They laugh, the tension of the past days lifting just a little."
    
    "Sana looks in her pockets, a pile of tournament earnings in cash and checks spread in front of her."
    sana "This is everything I've made so far. I could keep saving, playing smaller tournaments… or I could take the leap."
    sana "The Russian Invitational is my dream. If I win, it could change everything."
    sana "But if I lose… well, I've lost it all before."

    "Sana picks up her phone, glancing at Carter, who's busy tinkering with a chess set on the floor."
    sana "Carter, I think I'm going for it."
    carter "Going for what?"
    sana "Russia. The invite. I'm gambling everything I've earned so far."
    carter "That's a bold move. And by bold, I mean absolutely crazy. But it's also very Sana."
    sana "Are you saying I'm reckless?"
    carter "No, I'm saying you're fearless. Go for it. I'll be cheering for you from here."
    jump flight_to_russia

label flight_to_russia:
    scene airplane_interior with dissolve
    show sanaSprite at left
    "Sana stares out the airplane window, watching the clouds roll by. Her fingers tap nervously on the armrest."
    sana "This is it. The Russian Invitational. One shot to prove I belong here."
    sana "What if I freeze? What if I embarrass myself? What if…"
    "A stewardess walks by, and Sana forces herself to take a deep breath."
    sana "No. I've worked too hard for this. I just need to focus."
    "The sound of the pilot announcing their descent breaks her thoughts."
    sana "Here goes nothing."
    jump play_garry_kasparov
    
image russia_tournament_hall = im.Scale("russian_chess.jpg", 1920, 1080)

label play_garry_kasparov:
    scene russia_tournament_hall with dissolve
    play music "chess_thinking.mp3" loop
    "Sana sits across from Garry Kasparov in the grand tournament hall, the crowd murmuring in anticipation."
    show sanaSprite at left
    sana "This is insane. I'm sitting across from one of the greatest chess players of all time."
    "The game begins. Garry makes his first move, calm and calculated."
    menu:
        "Play conservatively in the opening.":
            sana "I need to play it safe and hold my position."
            "Sana struggles to defend as Garry pressures her relentlessly."
        "Try an aggressive opening.":
            sana "If I'm going down, I might as well go down swinging."
            "Her bold opening surprises Garry briefly, but he recovers with ease."

    "Sana feels herself stumbling as the game progresses, her mind racing to keep up."
    sana "He's overwhelming me. I can't keep up."
    "Suddenly, a familiar voice calls out from the crowd."
    show carterSprite at right
    carter "Come on, Sana! Show him what you've got!"
    "The tournament arbiters yell at him immediately and tell him to shush."
    sana "Carter? How is he here?"
    hide carterSprite
    "She glances up, spotting Carter waving enthusiastically. His presence brings a surge of energy."
    "Carter spent every last earning from his piggy bank and begged his parents to come. Who would have seen how far they have come."
    sana "He really came all this way… for me."

    "Sana refocuses, a newfound determination in her gaze."
    # Chess Theory Questions
    $ score = 0  

    "As the game reaches its climax, Kasparov challenges Sana with a series of complex chess problems."
    
    "Kasparov pushes his rook into position. 'If your opponent sacrifices a pawn to control the center, what’s your best counter-strategy?'"
    menu:
        "Control the center with your own pawn.":
            $ score += 1
        "Develop your pieces rapidly.":
            $ score += 0
        "Attack their king immediately.":
            $ score += 0
    
    "Kasparov smiles. 'An open file is created on the queenside. What’s the most effective use of this file?'"
    menu:
        "Move your rook to control the open file.":
            $ score += 1
        "Use your queen to dominate the board.":
            $ score += 0
        "Push your pawn to pressure the opponent.":
            $ score += 0
    
    "He nods. 'What's the best response to a fork on your king and queen?'"
    menu:
        "Move the king to avoid the fork.":
            $ score += 0
        "Sacrifice another piece to protect both.":
            $ score += 0
        "Counterattack the opponent's vulnerable piece.":
            $ score += 1

    "Kasparov continues. 'You’re ahead in material but behind in development. What’s your next move?'"
    menu:
        "Simplify the board by trading pieces.":
            $ score += 1
        "Push pawns aggressively to gain space.":
            $ score += 0
        "Focus on developing your pieces.":
            $ score += 0

    "He adjusts his glasses. 'What’s the key principle in a knight versus bishop endgame?'"
    menu:
        "Centralize the knight to increase its mobility.":
            $ score += 1
        "Keep your pawns on the same color as your bishop.":
            $ score += 0
        "Advance your king aggressively.":
            $ score += 0

    "Kasparov places his knight in a dangerous spot. 'How do you counter a knight outpost?'"
    menu:
        "Attack it with pawns to force it away.":
            $ score += 1
        "Trade it immediately with your knight.":
            $ score += 0
        "Ignore it and develop elsewhere.":
            $ score += 0

    "Final question. Kasparov leans back. 'You have a passed pawn. What’s your priority?'"
    menu:
        "Push it forward to promote.":
            $ score += 1
        "Use it as a decoy to attack elsewhere.":
            $ score += 0
        "Guard it with your king.":
            $ score += 0
    # Determine the outcome
    if score >= 5 and power_total > 300:
        jump kasparov_victory
    else:
        jump kasparov_defeat

label kasparov_victory:
    "Sana makes her final move, and the hall goes silent. Garry stares at the board for a moment before extending his hand."
    "Garry" "Congratulations. That was an exceptional game."
    sana "Did… I just beat Garry Kasparov?"
    "The crowd erupts in applause as Sana processes what just happened. Carter rushes to her side."
    show carterSprite at right
    carter "You did it! Sana, you beat him!"
    sana "I… I can't believe it."
    "As they walk out of the hall, Sana feels a mix of pride and disbelief, her name now etched in chess history."
    jump final_scene

label kasparov_defeat:
    "Sana makes her final move, but it's clear she's lost. Garry extends his hand with a kind smile."
    "Garry" "You played well. Few have lasted this long against me. Keep growing, and you'll go far."
    sana "I lost. But… I've never come this close before."
    "The crowd claps politely, and Carter comes to her side."
    show carterSprite at right
    carter "You did amazing, Sana. Don't let this get to you."
    sana "Thanks, Carter. I'll be back. Stronger than ever."
    "As they leave the hall, Sana feels determined to learn and grow from this experience, ready to take on the next challenge."
    jump final_scene
    
image airport = im.Scale("airport_moscow.jpg", 1920, 1080)

label final_scene:
    play music "seventies_love.mp3" loop
    scene airport with fade
    show sanaSprite at left
    show carterSprite at right
    sana "Well, Carter, I think it's safe to say I've completely explored the chess world."
    carter "Slightly joking, but it's true. I am so proud of you. I will always reminisce our battles when playing you used to be competitive."
    sana "HAHAH stop. You are still good."
    carter "The patrony...."
    sana "I didn't expect it to end like this, but... it feels right."
    stop music
    window hide
    $ renpy.pause(2)
    window show
    hide carterSprite
    
    play music "emotionalll.mp3" loop
    show momSprite at right

    "Elderly Woman" "Sana... is that you?"
    sana "Do I know you?"
    "Elderly Woman" "Ah, yes, I’ve heard you. You’re the young woman who won tournaments, one after another. Such a rise! Tell me, how did climb manage the ranks like that? The Wild Queen they call you."
    sana "It wasn't easy, but every win felt like a step closer to something bigger."
    "Elderly Woman" "It must have been a tough journey, each tournament harder than the last one. But you didn’t give up. That’s the sign of a true champion."

    sana "Yeah... I just kept pushing myself. Sometimes it felt like there was no end, but here I am."

    window hide
    $ renpy.pause(1)
    window show

    # Sana has the realization
    sana "Wait... her voice... her mannerisms... Why does she seem so familiar?"
    sana "No... it can’t be."

    sana "Mom?!"
    "Elderly Woman" "Sana... is it really you?"

    window hide
    $ renpy.pause(2)

    window show
    sana "I've missed you so much..."
    "Elderly Woman" "I've missed you too, my dear."
    sana "I thought you had to cut off ties because off politics."
    "Elderly Woman" "We will talk about it next time!"

    window hide
    scene black with fade
    stop music fadeout 2.0
    return

