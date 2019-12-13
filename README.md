# If Van Gogh was on Twitter

This project is about generating texts mimicking Vincent Van Gogh. This is
done using a Markov chain based on Van Gogh's letters.
 
 This project consists of two parts:
 
 - Building corpus
   - This is done in `get_data.py`. The dataset for this project consists of
    the letters of Vincent Van Gogh from the website http://vangoghletters.org/vg/ .
   Run this script to scrape the texts of the letters from the website. 
   Alternatively, you can straight away use the corpus in `vangogh_letters.txt`,
   which is the output of this script. In this file, each letter is contained
   on a single line.
 - Generating texts
    - This is done in `vangogh_tweets.py`, assuming that the corpus 
    `vangogh_letters.txt` has been outputted by `get_data.py`. This script
    creates a Markov chain of word transitions in the corpus. Instead of
    transitions from one word to another word, the transitions used are from
    a word to word bigrams. Then a sentence is randomly generated
    using the Markov chain. When a sentence is generated, it must adhere to
    a predetermined word count. The specified word count is randomly chosen
    from a list of sentence word counts in the corpus.
    
    
## Requirements
- beautifulsoup4
- nltk


## Sample generated texts
- Thus we’ll see.

- Lord is travelling, still cling to, which would give me you rely on a
 simple worshipper of the same profound compassion, in paris.
 
- The emptiness, of the hands of the world.

- I think i discern in it all the light falls — a certain trust me.

- Likely that it will be welcome to have nothing to do with this iron bars of
 paper or whatever.
 
- But equally, i know that life – artificial prolongation of this — to you
 refuse to have a gospel for a year.
 
- And the deaf, desperate state of painting. 

- Be able to give an eternal buddha.

- Going to come here and there be tongues, they shall i say.

- It’s like soapsuds, and unhappy with the process of reproduction.

- So accept this position, and we are not charming towards the end.

- She said that he was a tragedy and so are several accurate biographical
 details of your journey, i do more trust, more rooted and grey.
 
- What i might win and pull the chestnuts out of his would both much more
 beautiful italian portraits or imaginary switzerland.
 
- I want of something like that.

- The things tying me when i feel sad thing in red and the one sees meadows
 with haystacks. 

- Wish it in mind, you too, because he that followeth me shall manage’. 

- Was like you to have someone had injured himself in making something else. 

- Truly believe i could handle it all, but with a treasure, but some. 

- We see, when i still see it in arles.

- I say another word today to time.

- Wish to come from nature, wrestling with the practical use.

- There i feel my firm intention — i say, they came to be somewhere here, if
 he holds water.

- Longing to learn from the north, but the form.

- This week i got from you, christus consolator by scheffer, a photo of that
 i trampled on my acquaintances.

- They shall all know that i won’t retreat to somewhere else. 

- How much better than that i would rather be in the palace.

- Honest, manly approach and things.

- I don’t progress.

- It was abandoning me to promise you all my heart. 