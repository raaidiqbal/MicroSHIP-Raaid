# Potential Users:
- Anime Newcomers: Those who are new to anime and want to get their feet wet in the world of anime by searching for animes with good ratings and by looking for genres that match their interests.
- Anime Enthusiasts: The seasoned Anime enjoyers - anime enthusiasts have watched a number of anime and know their way around anime lingo, enabling them to easily search for the next anime that they want to watch.
- Anime Researchers: Those who are researching anime and want a robust way to get information quickly.

# Potential Benefits
- Users who are comfortable with a command line interface and HTML URLs can get a near instant answer to their queries.
- The ability to filter anime based on multiple genres allows users to tailor results to their specific tastes.
- Researchers can find information about the ratings and genres of various anime quickly.
- There is something for everyone; with our extremely large and comprehensive dataset, anime enjoyers will be able to find anime they will undoubtedly enjoy.


# CIDER Analysis

## This is our CIDER analysis for the Command Line deliverable. Four assumptions are analyzed here.

### Critique
The app assumes users will always know and input the exact titles of anime correctly, excluding users who do not remember the exact names of an anime. The app also assumes that users understand anime genres and are able to input them correctly for filtering purposes, which will make users who are new to anime or unfamiliar with specific genres excluded from using the app efficiently. Furthermore, the app assumes that all users are familiar with English, which excludes non-English speakers or users who are more comfortable in other languages, especially Japanese, the language of the media we are trying to make more accessible to users.


### Imagine
Users who don't remember the exact title of an anime or who misspell the title would not be able to retrieve the corresponding score and would not be able to get any use out of the software. Users who are new to anime or who don’t understand the distinctions between genres (e.g. the difference between "Shounen" and "Seinen") may struggle to use the genre-filtering feature effectively - thus would not be able to utilize the feature. Non-English-speaking users may find it difficult to use the app if they cannot read the instructions or understand the dataset's content, especially since the anime titles and genres are presented only in English.

### Design
To make the app software more inclusive, it could offer auto-complete suggestions or allow for partial title matches, which would help users find the anime they are looking for in a more efficient way and decrease the likelihood of bad input. This would help users who do not remember the exact title of an anime that they may be looking for.
To help users who are unfamiliar with anime genres, the app could provide the user with a sort of genre guide through help messages, or even predefined genre categories that users can select from, rather than requiring them to input genre names manually, thus making the software more accessible to users with varying levels of knowledge about anime, appealing to anime newcomers and anime enthusiasts.
Non-English speaking would benefit from the app adding support for multiple languages, providing localized versions of the command line prompts and dataset content for various languages, definitely including Japanese since a large amount of anime users are native-Japanese speakers. Users could select their preferred language when starting the app.

### Expand
We have learned about biases related to precision in user input in class, particularly that which has to do with less-abled users; the app may unintentionally exclude users who are prone to typos, such as people with less experience with typing or uncertain about the exact details of various anime.

### Repeat
We can also help out users who have difficulty typing titles correctly either because they are not very comfortable with typing or because they do not remember how to spell titles by implementing the previously mentioned auto-complete system which can complete the start of a title being typed in the command line.



# CIDER Analysis


## This is our additional CIDER analysis for the Flask deliverable. Three more assumptions are addressed here.


### Critique
The app assumes that users of the website are above a certain age appropriate to look up anime shows and movies that might contain unsavory content, themes and imagery such as gore and nudity. 
The app assumes that users are familiar with HTML URL percent encoding, or are using a browser that supports automatic conversion of "normal", standard-looking characters to HTML-encoded characters to make sure they are accessing the right destination. For instance, some browsers automatically convert spaces to the appropriate %20 for HTML.


### Imagine
Users who are under a certain age may be excluded from accessing anime shows and movies whose content is inappropriate for them because their parental figures may bar them from doing so. Therfore, a potential user's parents might not allow them to use the website, as it has no filters for different age ratings. Additionally, users of any age might not want to use the website out of concern that they might come across inappropriate content.
Users may input an anime title of two or more words that are separated by a space (or whatever symbol), which is not valid input for a URL. If users do not have a browser that automatically converts these spaces and symbols to their percent-encoded counterparts, they will not be able to access information about the score of an anime of their choice, meaning that they are excluded from half of our app's current functionality.


### Design
To make the website more inclusive, a dataset that includes age ratings for each of the listed anime shows and movies could allow us to add a filter by content rating function to allow more users to search for their desired anime, including young users whose parents may bar them from watching content above a certain rating.
Another feature that we could implement would be to automatically detect invalid input (spaces and special characters that are not formatted in their percent-encoded way) and replace them with their percent-encoded counterparts. This would help users who do not use a browser that automatically converts special characters and spaces to the proper HTML format and who are not familiar with HTML percent encoding to use the get_score function of our app.


### Expand
Users trust that our datasets are comprehensive and representative of anime watchers. They expect our data to be representative of various genres, studios, time periods, content types, and age groups, making searches conclusive and thorough.


### Repeat
We can do research on how the data was collected and provide a page that explains how the data was collected to assure users that the ratings are an accurate representation of what anime watchers think, that all genres are accurately represented, that there is an appropriately wide range of studios represented, both T.V. shows and movies are accurately represented, various time periods in anime are represented, and that different maturity ratings are represented. If, in our research, we find that one or more of these criteria is not met, we can explain the limitations of the dataset on a page on our website. We could also do research on other datasets that we could merge with the current one or to replace the current one in order to have a more comprehensive and representative dataset. Additionally, we could provide a feature that would allow users to suggest new anime to add to the website, which we would approve if we deem them valid. Furthermore, we can add a feature that allows users to provide their own score for an anime, which would be factored into the current score in the database.



# CIDER Analysis





## This is our additional CIDER analysis for the Database deliverable. Three more assumptions are addressed below.


### Critique
The dataset assumes that the users know the distinctions between anime sources: original, light novel, manga, web manga, 4-koma manga, visual novel, game, and picture book. 
Our dataset also assumes that users are interested in anime that are from the year 2020 or prior, which is when it was last updated. 


### Imagine
Users who are not aware of the anime source distinctions might not be able to benefit from its inclusion as a variable in the dataset; i.e., if a user does not know what anime source being manga is, they would not potentially benefit from looking up the manga version of the anime. 
Users that wish to search for animes from 2021 or later would be excluded by our website because there are none of these shows that exist in the database we are using, except for those that started in 2020 or prior and continued to 2021 or later. However, our database does not denote any of these said shows.


### Design
We can add a glossary of anime source terms to the website explaining what they mean. For example, the website should explain what manga is (essentially a Japanese comic book) and that the source being manga means that there is a comic book version of the anime out there with the same name. This would help out users who are unfamiliar with anime source names.
Additionally, to help include users that are looking for anime from 2021 or later, we could add anime that started in 2021 or later and update the air date for anime that started prior to 2020 but continued to at least 2021.


### Expand
 We have learned about how many websites assume some sort of baseline knowledge of the content that they contain. Consequently, we have learned the importance of explaining terms that, on their own, might exclude some users who are not familiar with the subject matter of the website we are designing. In our case, users who are not familiar with the names of animation studios would be excluded by our dataset if they are looking for a specific animation style.


### Repeat
Users that are looking for a specific animation style but are not familiar with the name of animation studios would be excluded because studios tend to have their own signature animation style. Therefore, if a user is only familiar with an animation style that they like and not a studio name, they may have trouble finding a particular animation style in our dataset when we eventually implement a feature allowing users to filter by studio. To help address this, we can create a table of all of the animation studios in our dataset with a brief description of their animation style, which we could display on a page on our website which can be accessed via a button on the homepage. This would allow the previously excluded users being discussed to figure out which studio(s) they are looking for.



---


# Potential Users for the functioning version of our website with a GUI (the Front End Deliverable):
- This is the same as the previous deliverables, except that our website now works for people with a variety of disabilities, as discussed in the last bullet point.
- Anime Newcomers: Those who are new to anime and want to get their feet wet in the world of anime by searching for animes with good ratings and by looking for genres that match their interests.
- Anime Enthusiasts: The seasoned Anime enjoyers - anime enthusiasts have watched a number of anime and know their way around anime lingo, enabling them to easily search for the next anime that they want to watch.
- Anime Researchers: Those who are researching anime and want a robust way to get information quickly.
- Additionally, our website has the ability to be used by people who use screen readers to navigate the web (thanks to our labels), people who are colorblind (thanks to our color scheme), people who have low vision (since our pages can be resized).

# Potential Benefits
- Users can find some basic information about a particular anime by typing its title in the search bar on the main page, such as the animation studio that produced it, its genres, or when it aired.
- If a user wishes to find an anime completely new to them, they can click on the "Random" button on the navigation bar, which will display information about a random anime from our database.
- Researchers can find basic information about virtually any particular anime that aired in 2020 or prior, and quickly if they know the title.

# CIDER Analysis


## This is our additional CIDER analysis for the Front-End deliverable. Two more assumptions are addressed here.

### Critique
Our website currently assumes that users know that our website is an interface to look through a database to search for anime shows and movies, as we don’t have a section that explains this right now.


### Imagine
Users who are not already aware of the website may not be able to immediately identify its purpose nor use the different features in the navigation bar that also rely on the user knowing how they pertain to the website itself. These users would be discouraged from using our website and excluded since they do not actually know what our website is.


### Design
We can add an “about” section to the website, so that users who are unfamiliar with it can identify what features it offers. This will allow users to properly understand the different parts of the website.


### Expand
Our website currently assumes that users know where they can watch anime.


### Repeat
A user may use the random button to find a random anime. However, in order for them to actually be able to watch the anime, they must have knowledge of a streaming service or T.V. channel where they can watch it, since we do not provide this information. This may exclude users that are new to watching anime and may not be familiar with streaming services that have anime to watch. These users would be excluded from obtaining the maximum amount of utility from our website. To help include these users, we could add a page reachable via a “Where to Watch Anime” tab in the navigation bar that displays a list of places where anime can be viewed.

