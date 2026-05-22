---
title: "Help:Contents"
archived_url: "https://web.archive.org/web/20110721115449/http://www.openlierox.net/wiki/index.php/Help:Contents"
last_modified: "12:50, 14 May 2008"
categories: [Moderation]
---
{% raw %}
# Help

This is the help section to get you started and adding articles. Read the guides on formatting first.

## General guidelines

You may add any relevant article in the wiki as long as you are a member of LXA and are logged in here. This wiki is primarily for Liero Xtreme related content and will be moderated accordingly. Changes made to the wiki are kept under moderation and violation of general good behaviour and codex will be adressed to accordingly. Violations may lead to a ban or mute here and/or LXA forums depending on the gravity of the crime. Just behave and you don't have to worry about that block of text.

When browsing the wiki, you might come across a red link. This means they are wanted articles. By clicking it you may start editing it and making the wiki a favour. If you wish to add anything else refer to [this](/wiki/index.php/Help_Contents/#adding_an_article) section.

## Making articles

These are guidelines that should be followed when making articles.
If you are ever unsure about the syntax, just look at the code of the page by pressing edit. Please look at the templates given on the main page as well. They are there to help the pages look presentable.

### Naming conventions

When making an article it should always spelled correctly and made with correct capitalisation.

:   :   **When naming a general article:**

* The first letter is always upper case.
* All words except names are lower case.
* Upper case is allowed if a word is part of the name of something.

:   :   :   For example: [[Liero Xtreme Alliance]] vs [[Category:Liero Xtreme community|]]
    :   **When naming a section of an article:**

* The same rules apply as for naming of general articles

:   :   **When making a new category:**

* The same rules apply for category naming as for general articles.

:   :   **When making a clan article:**

* The name of the clan article should be the clan's full name.
* The capital letters in the full name should be the ones that are upper case in the [clan tag](/wiki/index.php/Clan_tag/).
* If the name consists of one word only, the first letter should be upper case.
* If all letters in the clan tag are lower case, the first letter of the full name is upper case.
* Make an article with the clan tag, and have it redirect to the correctly name article.

### Article types

To read more specified articles on how to create articles of certain types, see the following subsections:

* Creating a user-article
* Creating a clan article
* Article discussion

### Formatting

Read: <http://en.wikipedia.org/wiki/Wikipedia:How_to_edit_a_page>

### Linking

In the text of your article, you may add links to articles that exist or should exist by putting the name of the article within double brackets ```` ```
[[Article]]
``` ````. Remember that the article link must be spelled exactly like the one you want to link to or it will show red.

Use the pipe to make the link show another text. Useful when adding clans or players, when the article name simply doesn't fit in the context, or when you want to add a work into the "link ink".

```` ```
[[Article|Link]]
``` ````

Example:

```` ```
I visit the [[Liero Xtreme Alliance|LXA forums]] every day.
``` ````

Gives the output:
I visit [LXA forums](/wiki/index.php/Liero_Xtreme_Alliance/) every day.
There should however always be an article with the with abbrevation of a long name if it is probable that anyone will search on it.

### Adding an article

Begin with checking the various general [categories](/wiki/index.php/Special_Categories/). If there is a category which fits the description of something you want to add, browse it and any subcategories for the item you would like to add.

* Place it in a fitting category

:   If you can't find it, chances are that there already is an article somewhere and uncategorized or with slightly different spelling;

* Use the search function. See the "page text matches".

:   If any of those articles is the one you want to add either;

    :   * Create a Redirection article with the string you used to search.

        :   :   *or*

        * Leave a comment with a better name if you think the article is poorly named. From there Moderators will see if the article should be moved

Else;

* Create the page.

## Categorizing

Every article should be in an appropriate category. Just put the code

```` ```
[[Category:<Insert category name here>]]
``` ````

in the top of the document and it will be placed in that category. An article can be in several categories, so put it where it's relevant.
If the category doesn't exist, and should; it should be made. Again, make sure the spelling of the category link is correct or it will just create a new one.
Also, a category may be in another category. To make a subcategory, simply go to the category article, and write.

```` ```
[[Category:<Insert category name here>]]
``` ````

**Note:** Some templates automatically categorise your clan. Make sure you check out what the templates do.

For more help check out [Categorizing](/wiki/index.php/Categorizing/)

## Redirecting

To redirect an article to another simply add the code to the *first line* of the page.

```` ```
#REDIRECT [[<Insert article name here>]]
``` ````

### Conventions

Try to avoid double redirects, i.e. try to redirect to the main article. So don't redirect an article to
another redirection article. Double redirections may occur if an article has been moved, however.
Bad redirects can be dealt with by checking these pages:
[BrokenRedirects](/wiki/index.php/Special_BrokenRedirects/)
[DoubleRedirects](/wiki/index.php/Special_DoubleRedirects/)

## Templates

Templates are articles which may be called from another article by using the {{Template}} command. All templates will be in the Templates namespace.
For example, the premade template [Test](/wiki/index.php/Template_Test/)

```` ```
{{Test}}
``` ````

Will generate the output:

This is a test template. Called from the article **Help:Contents**.

```
No parameter defined!
```

### Conventions

Templates are to have names of single words.

* The template name should describe where it's used.
* The first letter of the template should be uppercase.
* If the template name consists of more than one word, the first letter of each word should be upper case and the spaces removed.
{% endraw %}
