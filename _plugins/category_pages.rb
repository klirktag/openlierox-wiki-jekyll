# Generates a "Category:<Name>" page for every category referenced in the
# front matter of the wiki collection, mirroring MediaWiki's category pages.
#
# Each generated page lists the articles that belong to the category and is
# reachable at /wiki/index.php/Category_<Name>/ -- the same path the catlinks
# box at the bottom of every article links to.
module OpenLieroXWiki
  class CategoryPage < Jekyll::Page
    def initialize(site, category, members)
      @site = site
      @base = site.source
      @dir = "wiki/index.php/Category_#{category.gsub(' ', '_')}"
      @name = "index.html"

      process(@name)
      @data = {
        "layout" => "wiki",
        "title"  => "Category:#{category}",
      }

      members = members.sort_by { |m| m.data["title"].to_s.downcase }
      items = members.map do |m|
        url = m.url
        "<li><a href=\"#{url}\">#{m.data['title']}</a></li>"
      end.join("\n")

      @content = +""
      @content << "<p>The following #{members.size} "
      @content << (members.size == 1 ? "page is" : "pages are")
      @content << " in this category.</p>\n"
      @content << "<div class=\"pagelist\">\n<ul>\n#{items}\n</ul>\n</div>\n"
    end
  end

  class CategoryGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      wiki = site.collections["wiki"]
      return unless wiki

      buckets = Hash.new { |h, k| h[k] = [] }
      wiki.docs.each do |doc|
        Array(doc.data["categories"]).each do |cat|
          buckets[cat.to_s.strip] << doc unless cat.to_s.strip.empty?
        end
      end

      buckets.each do |category, members|
        site.pages << CategoryPage.new(site, category, members)
      end
    end
  end
end
