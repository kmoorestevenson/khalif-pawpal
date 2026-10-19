# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial class design included the classes Owner, Pet, Task, and Scheduler. Owner is the overall class that holds pets and a scheduler. Pet is a class that describes the pet and holds the pets tasks.  Scheduler is class that executes all of the scheduling algorithms such as filtering and prioritizing.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, my design changed when incorporating the scheduling algorithms because the scheduling algorithm needed a cut off date that will generate tasks up until that date.  Also, expired dates needed to be taken into account to include only future non-completed tasks on the schedule.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler tasks into account time and priority to the algorithm complexity to a minimum and limit the amount of data that the owner class contained.  I decided to prioritize date/time first then use priority as the tie-break.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The tradeoff I took into account was not taking into account user preferences to keep the algorithm complexity to a minimum and reduce the amount of data the owner class holds for know.  It is a reasonable tradeoff because it allows the user to properly prioritize tasks that they are inputting.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

The best prompts that helped were updating the code when I made changes to the UML.  Also, using to brainstorm a UML to get a basic structure of my applications architecture before coding.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
  I did not accept an AI suggestion when it prompted me to keep code that did not incorporate the proper name changes that I wanted.  I made sure to check the code diffs within the IDE before accepting them.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
  I made sure test that the owner can add pets, find pets, add tasks, remove tasks, and filter/prioritize tasks.  These tests were important to make sure new pets can be added, tasks can be added/removed properly without causing any issues, and properly filtering/prioritizing tasks for the owner.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
  I am pretty confident the scheduler can handle basic non-recurring tasks and pets with different names. I would definitely would like to test for recurring tasks and pets with same name but different types.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I was satisfied in the AI brainstorming process and building of the UML diagram. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had more time, take into account pets with the same name and different types.  Also, handle re-occurring tasks and tasks with a similar name.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
To use the UML diagram as a template to keep your code structured and using AI to build test cases based on the class methods.
