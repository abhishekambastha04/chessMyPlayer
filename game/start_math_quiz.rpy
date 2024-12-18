init python:
    class MathGameState:
        def __init__(self):
            self.math_score = 0
            self.current_question = 0
            self.player_answer = ""
            
    math_game = MathGameState()
    
    total_questions = 6
    time_per_question = 6.0

    math_problems = [
        ("What is 23 x 17", "391"),
        ("What is 125 - 67?", "58"),
        ("What is 91 × 8?", "728"),
        ("What is 35 x 8", "280"),
        ("What is 13 - 221?", "-208"),
        ("What is 16 + 467?", "493")
    ]

init:
    $ timer_range = 0
    $ timer_jump = False
    $ timer_limit = 6.0

screen countdown_timer:
    timer 0.1 action If(timer_range > 0, SetVariable("timer_range", timer_range - 0.1), Jump("process_timeout")) repeat True
    bar value timer_range range timer_limit xalign 0.5 ypos 50 xsize 400 ysize 20 

screen math_game_screen:
    modal True
    
    # Add the countdown timer
    use countdown_timer
        
    # Question display
    frame:
        xalign 0.5
        yalign 0.4
        padding (20, 20)
        
        vbox:
            spacing 20
            text "Question [math_game.current_question + 1] of [total_questions]" xalign 0.5
            text math_problems[math_game.current_question][0] xalign 0.5

            input default "" value math_game.player_answer:
                xalign 0.5
                length 10
                allow "0123456789"

    # Submit button
    textbutton "Submit":
        xalign 0.5
        yalign 0.6
        action [Hide("math_game_screen"), Jump("check_answer")]

# Changed label name to match the jump in script.rpy
label start_math_quiz:
    $ math_game.math_score = 0
    $ math_game.current_question = 0
    profConnor "Now, let's begin the mental math portion. You have 6 seconds per question."
    profConnor "Remember, quick thinking is essential!"
    
    jump show_question

label show_question:
    if math_game.current_question >= total_questions:
        jump quiz_complete
        
    $ math_game.player_answer = ""
    $ timer_range = timer_limit  # Reset timer
    $ renpy.show_screen("math_game_screen")
    $ ui.interact()  # Wait for input

label check_answer:
    $ given_answer = math_game.player_answer.strip()
    $ correct_answer = math_problems[math_game.current_question][1]
    
    if given_answer == correct_answer:
        $ math_game.math_score += 1
        "Correct!"
    else:
        "Incorrect. The answer was [correct_answer]."
    
    $ math_game.current_question += 1
    jump show_question

label process_timeout:
    hide screen math_game_screen
    "Time's up!"
    profConnor "Too slow! The correct answer was [math_problems[math_game.current_question][1]]."
    $ math_game.current_question += 1
    jump show_question

label quiz_complete:
    play music "tense.mp3" fadeout 1.0 fadein 1.0 loop
    profConnor "Quiz complete! You got [math_game.math_score] out of [total_questions] correct."
    
    if math_game.math_score >= 5:
        profConnor "Excellent work!"
    elif math_game.math_score >= 3:
        profConnor "You need more practice."
    else:
        profConnor "We'll need to schedule some tutoring sessions."
        
    stop music
    
    # Jump back to main script
    jump lunch_announcement