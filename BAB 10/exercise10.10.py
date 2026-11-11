#Common Words

sample_text = """
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep,
No more; and by a sleep to say we end
The heartache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream.
""".lower()

# Words to count
words_to_count = ["to", "be", "sleep", "die", "the", "and"]

print("Word frequency analysis (Hamlet excerpt):")
print("-" * 40)
for word in words_to_count:
    count = sample_text.count(word)
    print(f"  '{word}' appears {count} time(s).")
