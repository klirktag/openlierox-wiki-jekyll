# Rewrites root-relative links produced inside Markdown wiki content so that
# they respect site.baseurl when the site is deployed as a GitHub Pages
# project site (https://<user>.github.io/<repo>/).
#
# Converted wiki pages deliberately keep clean, human-readable links such as
#   [Liero 1.0](/wiki/index.php/Liero_1.0/)
#   ![screenshot](/wiki/images/6/66/Lmf.JPG)
# i.e. no Liquid noise in the Markdown. This hook adds the base path at build
# time. Links emitted by layouts already go through the `relative_url` filter
# (so they start with the baseurl) and are therefore left untouched.
Jekyll::Hooks.register [:documents, :pages], :post_render do |doc|
  baseurl = doc.site.config["baseurl"].to_s
  next if baseurl.empty?
  next unless doc.respond_to?(:output) && doc.output
  next unless (doc.respond_to?(:output_ext) ? doc.output_ext : ".html") == ".html"

  doc.output = doc.output.gsub(%r{\b(href|src)="(/(?:wiki|assets)/[^"]*)"}) do
    %(#{Regexp.last_match(1)}="#{baseurl}#{Regexp.last_match(2)}")
  end
end
