from bs4 import BeautifulSoup

soup = BeautifulSoup('''<div class="tasting-note-content">
      <div class="overlay-loading" style="display: none;"><img src="/wp-content/themes/james-suckling/img/ajax-loader.gif"></div>
      <input type="hidden" name="report_id" id="report_id" value="176415">
      <div class="tasting-note-response"><div class="entry-child-tasting_note access_note"><div class="show-btn" style="text-align:left;margin-bottom: 20px;">
                              
      <div class="col-xs-12 col-sm-12 col-md-12 tasting-note-sort-by" align="left" style="padding:0;float: right;width: auto;">
          <div id="filter-report-notes" class="filter-by">
            <span>FIND IN REPORT:</span>
            <input type="text" id="txt-filter" class="txt-filter clearable" placeholder="SEARCH THESE NOTES" value="" autocomplete="off">
            <div class="icon-filter"><span class="glyphicon glyphicon-filter"></span></div>
          </div>
          <div id="sort-report-notes" class="sort-by">
              <span>SORT BY:</span>
              <select id="select-sort-note" class=" access_note">
                        <option selected="\'true\'" value="rank_high" data-order="asc" data-expand="hide">RANK (HIGHEST FIRST)</option>
                        <option value="rank_low" data-order="desc" data-expand="hide">RANK (LOWEST FIRST)</option>
                            <option value="score_high" data-order="desc" data-expand="hide">SCORE (HIGHEST TO LOWEST)</option>
                            <option value="score_low" data-order="asc" data-expand="hide">SCORE (LOWEST TO HIGHEST)</option>
                            <option value="appellation_name" data-order="asc" data-expand="hide">WINE (A to Z)</option>
                            <option value="appellation_name" data-order="desc" data-expand="hide">WINE (Z to A)</option>
                            <option value="vintage_old" data-order="asc" data-expand="hide">VINTAGE (OLDEST FIRST)</option>
                            <option value="vintage_young" data-order="desc" data-expand="hide">VINTAGE (YOUNGEST FIRST)</option>
                        <option value="country_name" data-order="asc" data-expand="hide">COUNTRY (A to Z)</option>
                        <option value="country_name" data-order="desc" data-expand="hide">COUNTRY (Z to A)</option>
                </select>
        </div>
    </div>
  	    <button class="btn show-all" style="margin-top: 10px;"><i class="fa fa-eye"></i> | Expand Tasting Notes</button>
  			<button class="btn hide-all" style="display:none;margin-top: 10px;"><i class="fa fa-eye-slash"></i> | Hide Tasting Notes</button>
  			</div><div class="testing-notes-pagination-nav">
        <span class="testing-notes-showing">Showing <span class="page-number">1</span> to <span class="page-number">100</span> of <span class="page-number">100</span> notes </span>
        <div class="testing-notes-pagination">
            <ul>
            </ul>
        </div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-1">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-1" data-target="#collapse-1">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">1</span><span class="title-vintage">Kumeu River Chardonnay Kumeu Mate's Vineyard 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-1">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">New Zealand</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Kumeu</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Kumeu River Chardonnay Kumeu Mate's Vineyard/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is such impressive chardonnay in terms of power and complexity, delivering so much with such poise. Aromas of lemons and peaches intersect with lightly spicy oak and brioche on the nose. The palate drops mouth-filling flavors of peach and lemon and winds tight, before exploding long on the finish with a long, nutty afterglow. Perfect chardonnay. Drink over the next decade or more. Screw cap.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/159045/kumeu-river-chardonnay-kumeu-mates-vineyard-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_1"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159045%2Fkumeu-river-chardonnay-kumeu-mates-vineyard-2020%2F%3Fsid%3D866ceadfc4347f616d869edb138fdb2e&amp;linkname=Kumeu%20River%20Chardonnay%20Kumeu%20Mate%27s%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159045%2Fkumeu-river-chardonnay-kumeu-mates-vineyard-2020%2F%3Fsid%3D866ceadfc4347f616d869edb138fdb2e&amp;linkname=Kumeu%20River%20Chardonnay%20Kumeu%20Mate%27s%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159045%2Fkumeu-river-chardonnay-kumeu-mates-vineyard-2020%2F%3Fsid%3D866ceadfc4347f616d869edb138fdb2e&amp;linkname=Kumeu%20River%20Chardonnay%20Kumeu%20Mate%27s%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159045%2Fkumeu-river-chardonnay-kumeu-mates-vineyard-2020%2F%3Fsid%3D866ceadfc4347f616d869edb138fdb2e&amp;linkname=Kumeu%20River%20Chardonnay%20Kumeu%20Mate%27s%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a>
<script type="text/javascript"><!--
if(wpa2a)wpa2a.script_load();
//--></script>
<script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Kumeu River Chardonnay Kumeu Mate's Vineyard",url:"https://www.jamessuckling.com/tasting-notes/159045/kumeu-river-chardonnay-kumeu-mates-vineyard-2020/?sid=866ceadfc4347f616d869edb138fdb2e"});

if('function'===typeof(jQuery))jQuery(document).ready(function($){$('body').on('post-load',function(){if(wpa2a.script_ready)wpa2a.init();wpa2a.script_load();});});
//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-2">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-2" data-target="#collapse-2">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">2</span><span class="title-vintage">Barone Ricasoli Chianti Classico Gran Selezione Ceniprimo 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-2">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Barone Ricasoli Chianti Classico Gran Selezione Ceniprimo/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is amazing Chianti Classico. Perhaps the greatest I have ever tasted. The aromas are so complex with crushed cherries, sour cherries, peaches, bark and hints of meat. Incredible finish with such intensity and beauty. Hard not to drink, but one for the cellar. Best after 2024.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/153457/barone-ricasoli-chianti-classico-gran-selezione-ceniprimo-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_2"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153457%2Fbarone-ricasoli-chianti-classico-gran-selezione-ceniprimo-2018%2F%3Fsid%3D153d6eadc92ffac39c10b4013aa1b9bc&amp;linkname=Barone%20Ricasoli%20Chianti%20Classico%20Gran%20Selezione%20Ceniprimo" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153457%2Fbarone-ricasoli-chianti-classico-gran-selezione-ceniprimo-2018%2F%3Fsid%3D153d6eadc92ffac39c10b4013aa1b9bc&amp;linkname=Barone%20Ricasoli%20Chianti%20Classico%20Gran%20Selezione%20Ceniprimo" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153457%2Fbarone-ricasoli-chianti-classico-gran-selezione-ceniprimo-2018%2F%3Fsid%3D153d6eadc92ffac39c10b4013aa1b9bc&amp;linkname=Barone%20Ricasoli%20Chianti%20Classico%20Gran%20Selezione%20Ceniprimo" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153457%2Fbarone-ricasoli-chianti-classico-gran-selezione-ceniprimo-2018%2F%3Fsid%3D153d6eadc92ffac39c10b4013aa1b9bc&amp;linkname=Barone%20Ricasoli%20Chianti%20Classico%20Gran%20Selezione%20Ceniprimo" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Barone Ricasoli Chianti Classico Gran Selezione Ceniprimo",url:"https://www.jamessuckling.com/tasting-notes/153457/barone-ricasoli-chianti-classico-gran-selezione-ceniprimo-2018/?sid=153d6eadc92ffac39c10b4013aa1b9bc"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-3">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-3" data-target="#collapse-3">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">3</span><span class="title-vintage">Dönnhoff Riesling Nahe Hermannshöhle GG 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-3">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Nahe</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Dönnhoff Riesling Nahe Hermannshöhle GG/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">The greatest wines are clear right from the very beginning, because not only is there a super abundance of perfect ripeness, but everything fits so beautifully that you’re instantly captivated. That’s exactly the way this dry riesling masterpiece is. The most ravishing, peachy fruit and the most perfect balance. Then comes the totally compelling, salty finish that just doesn’t want to stop. From organically grown grapes with Fair'n Green certification. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/157932/donnhoff-riesling-nahe-hermannshohle-gg-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_3"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157932%2Fdonnhoff-riesling-nahe-hermannshohle-gg-2020%2F%3Fsid%3D757d393d996b139d58d57b1bb986af41&amp;linkname=D%C3%B6nnhoff%20Riesling%20Nahe%20Hermannsh%C3%B6hle%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157932%2Fdonnhoff-riesling-nahe-hermannshohle-gg-2020%2F%3Fsid%3D757d393d996b139d58d57b1bb986af41&amp;linkname=D%C3%B6nnhoff%20Riesling%20Nahe%20Hermannsh%C3%B6hle%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157932%2Fdonnhoff-riesling-nahe-hermannshohle-gg-2020%2F%3Fsid%3D757d393d996b139d58d57b1bb986af41&amp;linkname=D%C3%B6nnhoff%20Riesling%20Nahe%20Hermannsh%C3%B6hle%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157932%2Fdonnhoff-riesling-nahe-hermannshohle-gg-2020%2F%3Fsid%3D757d393d996b139d58d57b1bb986af41&amp;linkname=D%C3%B6nnhoff%20Riesling%20Nahe%20Hermannsh%C3%B6hle%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"D\u00f6nnhoff Riesling Nahe Hermannsh\u00f6hle GG",url:"https://www.jamessuckling.com/tasting-notes/157932/donnhoff-riesling-nahe-hermannshohle-gg-2020/?sid=757d393d996b139d58d57b1bb986af41"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-4">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-4" data-target="#collapse-4">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">4</span><span class="title-vintage">Mount Mary Yarra Valley Quintet 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-4">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Victoria</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Mount Mary Yarra Valley Quintet/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is a great Quintet, one of the best in fact. Here’s a wine that combines such elegance, power and polish to a level seen in the best wines of Bordeaux in the best vintages. Aromas of blueberries, cassis and mulberries are framed in cedar and fresh, leafy cabernet tones, as well as violets and forest wood. Some subtle oak spice here, too. The palate is so seamlessly layered with ultra-fine tannins that carry pristine blueberry, redcurrant and blackcurrant flavors. Concentrated, with pitch-perfect balance. Acidity imbues the finish with freshness and vitality. So elegant and unwavering. A Yarra Valley First Growth! Delicious now, but try from 2027 and for a decade after that.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/166158/mount-mary-yarra-valley-quintet-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_4"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166158%2Fmount-mary-yarra-valley-quintet-2019%2F%3Fsid%3D64790a3cd52d43da6cd75cf89f3640a0&amp;linkname=Mount%20Mary%20Yarra%20Valley%20Quintet" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166158%2Fmount-mary-yarra-valley-quintet-2019%2F%3Fsid%3D64790a3cd52d43da6cd75cf89f3640a0&amp;linkname=Mount%20Mary%20Yarra%20Valley%20Quintet" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166158%2Fmount-mary-yarra-valley-quintet-2019%2F%3Fsid%3D64790a3cd52d43da6cd75cf89f3640a0&amp;linkname=Mount%20Mary%20Yarra%20Valley%20Quintet" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166158%2Fmount-mary-yarra-valley-quintet-2019%2F%3Fsid%3D64790a3cd52d43da6cd75cf89f3640a0&amp;linkname=Mount%20Mary%20Yarra%20Valley%20Quintet" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Mount Mary Yarra Valley Quintet",url:"https://www.jamessuckling.com/tasting-notes/166158/mount-mary-yarra-valley-quintet-2019/?sid=64790a3cd52d43da6cd75cf89f3640a0"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-5">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-5" data-target="#collapse-5">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">5</span><span class="title-vintage">Aubert Chardonnay Napa Valley Sugar Shack Estate Vineyard 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-5">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Aubert Chardonnay Napa Valley Sugar Shack Estate Vineyard/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Such an aromatic nose of fresh hay, meyer lemon, baked green apple and dried herbs. Full-bodied with such an incredible amount of refinement. Sleek and seamless. Nuanced is an understatement, as this wine carries multitudes, quietly expressing flavors of fennel seed, dried lily, honeysuckle, toasted almond and sage. Incredible. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/168125/aubert-chardonnay-napa-valley-sugar-shack-estate-vineyard-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_5"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F168125%2Faubert-chardonnay-napa-valley-sugar-shack-estate-vineyard-2019%2F%3Fsid%3D631ceaef532591da2caadae0ed20b208&amp;linkname=Aubert%20Chardonnay%20Napa%20Valley%20Sugar%20Shack%20Estate%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F168125%2Faubert-chardonnay-napa-valley-sugar-shack-estate-vineyard-2019%2F%3Fsid%3D631ceaef532591da2caadae0ed20b208&amp;linkname=Aubert%20Chardonnay%20Napa%20Valley%20Sugar%20Shack%20Estate%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F168125%2Faubert-chardonnay-napa-valley-sugar-shack-estate-vineyard-2019%2F%3Fsid%3D631ceaef532591da2caadae0ed20b208&amp;linkname=Aubert%20Chardonnay%20Napa%20Valley%20Sugar%20Shack%20Estate%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F168125%2Faubert-chardonnay-napa-valley-sugar-shack-estate-vineyard-2019%2F%3Fsid%3D631ceaef532591da2caadae0ed20b208&amp;linkname=Aubert%20Chardonnay%20Napa%20Valley%20Sugar%20Shack%20Estate%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Aubert Chardonnay Napa Valley Sugar Shack Estate Vineyard",url:"https://www.jamessuckling.com/tasting-notes/168125/aubert-chardonnay-napa-valley-sugar-shack-estate-vineyard-2019/?sid=631ceaef532591da2caadae0ed20b208"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-6">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-6" data-target="#collapse-6">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">6</span><span class="title-vintage">Continuum Napa Valley Sage Mountain Vineyard 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-6">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Continuum Napa Valley Sage Mountain Vineyard/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This has incredible nuances and delicacy with power. It’s full-bodied with lots of gentle tannins that spread across the palate. The character is full of blackberry, blackcurrant and lead pencil. Some conifer and pine needles. Sage at the end, too. Savory. So long-lasting and layered. Such purity. It’s so complex and changes all the time in the glass. Goes on for minutes. 54% cabernet sauvignon, 31% cabernet franc, 9% petit verdot and 6% merlot. Organically grown grapes. So drinkable now, but will age beautifully.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/154554/continuum-napa-valley-sage-mountain-vineyard-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_6"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154554%2Fcontinuum-napa-valley-sage-mountain-vineyard-2018%2F%3Fsid%3D8efcf2545418a63af736b883b9e9d5bf&amp;linkname=Continuum%20Napa%20Valley%20Sage%20Mountain%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154554%2Fcontinuum-napa-valley-sage-mountain-vineyard-2018%2F%3Fsid%3D8efcf2545418a63af736b883b9e9d5bf&amp;linkname=Continuum%20Napa%20Valley%20Sage%20Mountain%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154554%2Fcontinuum-napa-valley-sage-mountain-vineyard-2018%2F%3Fsid%3D8efcf2545418a63af736b883b9e9d5bf&amp;linkname=Continuum%20Napa%20Valley%20Sage%20Mountain%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154554%2Fcontinuum-napa-valley-sage-mountain-vineyard-2018%2F%3Fsid%3D8efcf2545418a63af736b883b9e9d5bf&amp;linkname=Continuum%20Napa%20Valley%20Sage%20Mountain%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Continuum Napa Valley Sage Mountain Vineyard",url:"https://www.jamessuckling.com/tasting-notes/154554/continuum-napa-valley-sage-mountain-vineyard-2018/?sid=8efcf2545418a63af736b883b9e9d5bf"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-7">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-7" data-target="#collapse-7">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">7</span><span class="title-vintage">Taittinger Champagne Comtes de Champagne Blanc de Blancs 2008</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-7">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Champagne</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2008</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Taittinger Champagne Comtes de Champagne Blanc de Blancs/2008/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">The perfect blanc de blancs. Full-bodied with a lovely framework of acidity and dry fruit, such as apples, pears and peaches. Opulent. Dense and muscular. Yet, it’s balanced and harmonious. Line of acidity at the end. Totally in tune. Superb. Deep and complete. Has everything. One for the cellar. It is the greatest Comte ever. It has everything. A perfect upgrade from two years ago. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149961/taittinger-champagne-comtes-de-champagne-blanc-de-blancs-2008">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_7"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149961%2Ftaittinger-champagne-comtes-de-champagne-blanc-de-blancs-2008%2F%3Fsid%3Dabaf7a2235387c6416d86e2c44e3ef10&amp;linkname=Taittinger%20Champagne%20Comtes%20de%20Champagne%20Blanc%20de%20Blancs" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149961%2Ftaittinger-champagne-comtes-de-champagne-blanc-de-blancs-2008%2F%3Fsid%3Dabaf7a2235387c6416d86e2c44e3ef10&amp;linkname=Taittinger%20Champagne%20Comtes%20de%20Champagne%20Blanc%20de%20Blancs" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149961%2Ftaittinger-champagne-comtes-de-champagne-blanc-de-blancs-2008%2F%3Fsid%3Dabaf7a2235387c6416d86e2c44e3ef10&amp;linkname=Taittinger%20Champagne%20Comtes%20de%20Champagne%20Blanc%20de%20Blancs" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149961%2Ftaittinger-champagne-comtes-de-champagne-blanc-de-blancs-2008%2F%3Fsid%3Dabaf7a2235387c6416d86e2c44e3ef10&amp;linkname=Taittinger%20Champagne%20Comtes%20de%20Champagne%20Blanc%20de%20Blancs" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Taittinger Champagne Comtes de Champagne Blanc de Blancs",url:"https://www.jamessuckling.com/tasting-notes/149961/taittinger-champagne-comtes-de-champagne-blanc-de-blancs-2008/?sid=abaf7a2235387c6416d86e2c44e3ef10"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-8">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-8" data-target="#collapse-8">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">8</span><span class="title-vintage">Romano Dal Forno Amarone della Valpolicella Monte Lodoletta 2015</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-8">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Veneto</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2015</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Romano Dal Forno Amarone della Valpolicella Monte Lodoletta/2015/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is black as pitch in the glass and, yes, there’s a light, tarry edge to the super-concentrated prune, date and currant fruit. But even more interesting are the complex notes of bitter-orange liqueur, aged balsamic, fresh roasting herbs, cinnamon, roasted chestnuts, black tea and licorice. The more you decant in advance, the more nuances will emerge. It’s full-boded with huge concentration and lots of chewy tannin that is managing to hold the fruit back for now. This needs plenty of time to develop in the bottle. Just superb. One of the greatest Dal Forno’s ever.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/156893/romano-dal-forno-amarone-della-valpolicella-monte-lodoletta-2015">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_8"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156893%2Fromano-dal-forno-amarone-della-valpolicella-monte-lodoletta-2015%2F%3Fsid%3Dbd48b977de8f228c4e6021ef4e1fcf75&amp;linkname=Romano%20Dal%20Forno%20Amarone%20della%20Valpolicella%20Monte%20Lodoletta" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156893%2Fromano-dal-forno-amarone-della-valpolicella-monte-lodoletta-2015%2F%3Fsid%3Dbd48b977de8f228c4e6021ef4e1fcf75&amp;linkname=Romano%20Dal%20Forno%20Amarone%20della%20Valpolicella%20Monte%20Lodoletta" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156893%2Fromano-dal-forno-amarone-della-valpolicella-monte-lodoletta-2015%2F%3Fsid%3Dbd48b977de8f228c4e6021ef4e1fcf75&amp;linkname=Romano%20Dal%20Forno%20Amarone%20della%20Valpolicella%20Monte%20Lodoletta" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156893%2Fromano-dal-forno-amarone-della-valpolicella-monte-lodoletta-2015%2F%3Fsid%3Dbd48b977de8f228c4e6021ef4e1fcf75&amp;linkname=Romano%20Dal%20Forno%20Amarone%20della%20Valpolicella%20Monte%20Lodoletta" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Romano Dal Forno Amarone della Valpolicella Monte Lodoletta",url:"https://www.jamessuckling.com/tasting-notes/156893/romano-dal-forno-amarone-della-valpolicella-monte-lodoletta-2015/?sid=bd48b977de8f228c4e6021ef4e1fcf75"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-9">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-9" data-target="#collapse-9">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">9</span><span class="title-vintage">Dominus Napa Valley  2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-9">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Dominus Napa Valley /2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is incredible on the nose, offering hot stones, blackcurrants, iodine and wet earth. Full-bodied with a tight center palate, then it opens with a tannin structure that is weightless and spreads across the palate. Totally integrated on the palate. This is a magic-carpet wine. Really incredible. One of the reference points for the vintage.  Drinkable now and please try a bottle, but it’s one for the cellar.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/154160/dominus-napa-valley-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_9"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154160%2Fdominus-napa-valley-2018%2F%3Fsid%3D1f81f86a696ce4cc84df98cffb8ce28d&amp;linkname=Dominus%20Napa%20Valley%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154160%2Fdominus-napa-valley-2018%2F%3Fsid%3D1f81f86a696ce4cc84df98cffb8ce28d&amp;linkname=Dominus%20Napa%20Valley%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154160%2Fdominus-napa-valley-2018%2F%3Fsid%3D1f81f86a696ce4cc84df98cffb8ce28d&amp;linkname=Dominus%20Napa%20Valley%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154160%2Fdominus-napa-valley-2018%2F%3Fsid%3D1f81f86a696ce4cc84df98cffb8ce28d&amp;linkname=Dominus%20Napa%20Valley%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Dominus Napa Valley ",url:"https://www.jamessuckling.com/tasting-notes/154160/dominus-napa-valley-2018/?sid=1f81f86a696ce4cc84df98cffb8ce28d"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-10">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-10" data-target="#collapse-10">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">10</span><span class="title-vintage">Château Trotanoy Pomerol 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-10">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Trotanoy Pomerol/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Super nose of dried blueberry, black plum, walnut, myrrh and sandalwood. Lavender, violet, and chocolate, too. Ripe with wood now, but fresh. It’s full-bodied with firm, ultra fine tannins. Lots of dark spice is interlaced with the ripe fruit, giving this complex, perfumed character. Muscular, long and seamless with incredible depth and concentration. Reminds me of the great 2009, but this is better with more structure. Amazing wine. This is 100% merlot. Try from 2027.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145110/chateau-trotanoy-pomerol-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_10"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145110%2Fchateau-trotanoy-pomerol-2018%2F%3Fsid%3D4cde5c530be24b8dee49ee814f721bf4&amp;linkname=Ch%C3%A2teau%20Trotanoy%20Pomerol" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145110%2Fchateau-trotanoy-pomerol-2018%2F%3Fsid%3D4cde5c530be24b8dee49ee814f721bf4&amp;linkname=Ch%C3%A2teau%20Trotanoy%20Pomerol" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145110%2Fchateau-trotanoy-pomerol-2018%2F%3Fsid%3D4cde5c530be24b8dee49ee814f721bf4&amp;linkname=Ch%C3%A2teau%20Trotanoy%20Pomerol" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145110%2Fchateau-trotanoy-pomerol-2018%2F%3Fsid%3D4cde5c530be24b8dee49ee814f721bf4&amp;linkname=Ch%C3%A2teau%20Trotanoy%20Pomerol" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Trotanoy Pomerol",url:"https://www.jamessuckling.com/tasting-notes/145110/chateau-trotanoy-pomerol-2018/?sid=4cde5c530be24b8dee49ee814f721bf4"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-11">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-11" data-target="#collapse-11">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">11</span><span class="title-vintage">Compañia de Vinos Telmo Rodriguez Rioja Las Beatas 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-11">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Spain</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">La Rioja</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Compañia de Vinos Telmo Rodriguez Rioja Las Beatas/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is incredible on the nose with fresh flowers, spices, pure dark fruit and hints of stones. Full-bodied and so refined and polished with such intensity and length. Just goes on and on ... forever. A magical wine. From organically grown grapes. Please leave it for five or six years, if you can.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/160534/compania-de-vinos-telmo-rodriguez-rioja-las-beatas-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_11"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160534%2Fcompania-de-vinos-telmo-rodriguez-rioja-las-beatas-2018%2F%3Fsid%3D0349701a38793c4e3e32cfc1d8d59d96&amp;linkname=Compa%C3%B1ia%20de%20Vinos%20Telmo%20Rodriguez%20Rioja%20Las%20Beatas" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160534%2Fcompania-de-vinos-telmo-rodriguez-rioja-las-beatas-2018%2F%3Fsid%3D0349701a38793c4e3e32cfc1d8d59d96&amp;linkname=Compa%C3%B1ia%20de%20Vinos%20Telmo%20Rodriguez%20Rioja%20Las%20Beatas" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160534%2Fcompania-de-vinos-telmo-rodriguez-rioja-las-beatas-2018%2F%3Fsid%3D0349701a38793c4e3e32cfc1d8d59d96&amp;linkname=Compa%C3%B1ia%20de%20Vinos%20Telmo%20Rodriguez%20Rioja%20Las%20Beatas" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160534%2Fcompania-de-vinos-telmo-rodriguez-rioja-las-beatas-2018%2F%3Fsid%3D0349701a38793c4e3e32cfc1d8d59d96&amp;linkname=Compa%C3%B1ia%20de%20Vinos%20Telmo%20Rodriguez%20Rioja%20Las%20Beatas" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Compa\u00f1ia de Vinos Telmo Rodriguez Rioja Las Beatas",url:"https://www.jamessuckling.com/tasting-notes/160534/compania-de-vinos-telmo-rodriguez-rioja-las-beatas-2018/?sid=0349701a38793c4e3e32cfc1d8d59d96"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-12">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-12" data-target="#collapse-12">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">12</span><span class="title-vintage">Joh. Jos. Prum Riesling Mosel Wehlener Sonnenuhr Auslese Gold Cap 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-12">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Mosel</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Joh. Jos. Prum Riesling Mosel Wehlener Sonnenuhr Auslese Gold Cap/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Welcome to one of the most beautiful faces of the Mosel. Essence of yellow fruit, from peach through mango to papaya. So concentrated, yet so vibrant and so pristine with such a mind-boggling number of nuances that your nervous system is pushed to the limit, in the nicest possible way. The generous sweetness is already well integrated, but this is made for the many decades to come. Drinkable now, but better from 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149960/joh-jos-prum-riesling-mosel-wehlener-sonnenuhr-auslese-gold-cap-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_12"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149960%2Fjoh-jos-prum-riesling-mosel-wehlener-sonnenuhr-auslese-gold-cap-2019%2F%3Fsid%3D542d8bc1d8860bc0b8a8cac668616fc0&amp;linkname=Joh.%20Jos.%20Prum%20Riesling%20Mosel%20Wehlener%20Sonnenuhr%20Auslese%20Gold%20Cap" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149960%2Fjoh-jos-prum-riesling-mosel-wehlener-sonnenuhr-auslese-gold-cap-2019%2F%3Fsid%3D542d8bc1d8860bc0b8a8cac668616fc0&amp;linkname=Joh.%20Jos.%20Prum%20Riesling%20Mosel%20Wehlener%20Sonnenuhr%20Auslese%20Gold%20Cap" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149960%2Fjoh-jos-prum-riesling-mosel-wehlener-sonnenuhr-auslese-gold-cap-2019%2F%3Fsid%3D542d8bc1d8860bc0b8a8cac668616fc0&amp;linkname=Joh.%20Jos.%20Prum%20Riesling%20Mosel%20Wehlener%20Sonnenuhr%20Auslese%20Gold%20Cap" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149960%2Fjoh-jos-prum-riesling-mosel-wehlener-sonnenuhr-auslese-gold-cap-2019%2F%3Fsid%3D542d8bc1d8860bc0b8a8cac668616fc0&amp;linkname=Joh.%20Jos.%20Prum%20Riesling%20Mosel%20Wehlener%20Sonnenuhr%20Auslese%20Gold%20Cap" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Joh. Jos. Prum Riesling Mosel Wehlener Sonnenuhr Auslese Gold Cap",url:"https://www.jamessuckling.com/tasting-notes/149960/joh-jos-prum-riesling-mosel-wehlener-sonnenuhr-auslese-gold-cap-2019/?sid=542d8bc1d8860bc0b8a8cac668616fc0"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-13">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-13" data-target="#collapse-13">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">13</span><span class="title-vintage">Yangarra Grenache McLaren Vale Ovitelli 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-13">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">South Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Yangarra Grenache McLaren Vale Ovitelli/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Such attractive red-floral, stone and bracken aromas here with a red-plum and redcurrant edge, as well as pink grapefruit, blood orange and white pepper. The palate has a sleek and granular feel with a finely detailed style of tannin and a dried red-berry and cherry core. Leaf-like layers of tannin. Exquisite. Drink over the next eight years. Screw cap.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/161430/yangarra-grenache-mclaren-vale-ovitelli-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_13"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161430%2Fyangarra-grenache-mclaren-vale-ovitelli-2019%2F%3Fsid%3D85f71c267b06ee7fe4e908da32dcf8a6&amp;linkname=Yangarra%20Grenache%20McLaren%20Vale%20Ovitelli" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161430%2Fyangarra-grenache-mclaren-vale-ovitelli-2019%2F%3Fsid%3D85f71c267b06ee7fe4e908da32dcf8a6&amp;linkname=Yangarra%20Grenache%20McLaren%20Vale%20Ovitelli" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161430%2Fyangarra-grenache-mclaren-vale-ovitelli-2019%2F%3Fsid%3D85f71c267b06ee7fe4e908da32dcf8a6&amp;linkname=Yangarra%20Grenache%20McLaren%20Vale%20Ovitelli" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161430%2Fyangarra-grenache-mclaren-vale-ovitelli-2019%2F%3Fsid%3D85f71c267b06ee7fe4e908da32dcf8a6&amp;linkname=Yangarra%20Grenache%20McLaren%20Vale%20Ovitelli" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Yangarra Grenache McLaren Vale Ovitelli",url:"https://www.jamessuckling.com/tasting-notes/161430/yangarra-grenache-mclaren-vale-ovitelli-2019/?sid=85f71c267b06ee7fe4e908da32dcf8a6"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-14">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-14" data-target="#collapse-14">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">14</span><span class="title-vintage">Schloss Johannisberg Riesling Rheingau Grünlack Spätlese 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-14">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Rheingau</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Schloss Johannisberg Riesling Rheingau Grünlack Spätlese/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Very cool and reserved at the front, but this is an enormously deep and complex wine that has staggering mineral intensity. The lime and oolong-tea freshness effortlessly swallows up the unfermented grape sweetness, as if it didn’t really exist. Some will criticize, saying that this is too radical, but that’s what creates the great excitement! The herbal freshness at the finish is really astounding. Drinkable now, but best from 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/156894/schloss-johannisberg-riesling-rheingau-grunlack-spatlese-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_14"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156894%2Fschloss-johannisberg-riesling-rheingau-grunlack-spatlese-2020%2F%3Fsid%3D3d382d7fa55ea951b19322c6d5471ddc&amp;linkname=Schloss%20Johannisberg%20Riesling%20Rheingau%20Gr%C3%BCnlack%20Sp%C3%A4tlese" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156894%2Fschloss-johannisberg-riesling-rheingau-grunlack-spatlese-2020%2F%3Fsid%3D3d382d7fa55ea951b19322c6d5471ddc&amp;linkname=Schloss%20Johannisberg%20Riesling%20Rheingau%20Gr%C3%BCnlack%20Sp%C3%A4tlese" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156894%2Fschloss-johannisberg-riesling-rheingau-grunlack-spatlese-2020%2F%3Fsid%3D3d382d7fa55ea951b19322c6d5471ddc&amp;linkname=Schloss%20Johannisberg%20Riesling%20Rheingau%20Gr%C3%BCnlack%20Sp%C3%A4tlese" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156894%2Fschloss-johannisberg-riesling-rheingau-grunlack-spatlese-2020%2F%3Fsid%3D3d382d7fa55ea951b19322c6d5471ddc&amp;linkname=Schloss%20Johannisberg%20Riesling%20Rheingau%20Gr%C3%BCnlack%20Sp%C3%A4tlese" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Schloss Johannisberg Riesling Rheingau Gr\u00fcnlack Sp\u00e4tlese",url:"https://www.jamessuckling.com/tasting-notes/156894/schloss-johannisberg-riesling-rheingau-grunlack-spatlese-2020/?sid=3d382d7fa55ea951b19322c6d5471ddc"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-15">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-15" data-target="#collapse-15">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">15</span><span class="title-vintage">Cristom Pinot Noir Willamette Valley Eola-Amity Hills Jessie Vineyard 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-15">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Oregon</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Cristom Pinot Noir Willamette Valley Eola-Amity Hills Jessie Vineyard/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This dramatically steep site delivers a wine of real personality and distinctiveness. The nose has a very layered mix of red cherries and berries with some plums, leaves, dry stones, forest wood and a wealth of sweetly fragrant spices. The palate holds such intensity and concentrated flavor with striking focus and drive. Mouthwateringly fresh red-cherry flavors are delivered in essence-like mode and hold long, on a super vibrant, explosive finish. The star of 2018 at Cristom and indeed for Willamette Valley pinot per se. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/156248/cristom-pinot-noir-willamette-valley-eola-amity-hills-jessie-vineyard-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_15"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156248%2Fcristom-pinot-noir-willamette-valley-eola-amity-hills-jessie-vineyard-2018%2F%3Fsid%3D397ec86755cddae1cbdcaa5c47e7f0c6&amp;linkname=Cristom%20Pinot%20Noir%20Willamette%20Valley%20Eola-Amity%20Hills%20Jessie%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156248%2Fcristom-pinot-noir-willamette-valley-eola-amity-hills-jessie-vineyard-2018%2F%3Fsid%3D397ec86755cddae1cbdcaa5c47e7f0c6&amp;linkname=Cristom%20Pinot%20Noir%20Willamette%20Valley%20Eola-Amity%20Hills%20Jessie%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156248%2Fcristom-pinot-noir-willamette-valley-eola-amity-hills-jessie-vineyard-2018%2F%3Fsid%3D397ec86755cddae1cbdcaa5c47e7f0c6&amp;linkname=Cristom%20Pinot%20Noir%20Willamette%20Valley%20Eola-Amity%20Hills%20Jessie%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156248%2Fcristom-pinot-noir-willamette-valley-eola-amity-hills-jessie-vineyard-2018%2F%3Fsid%3D397ec86755cddae1cbdcaa5c47e7f0c6&amp;linkname=Cristom%20Pinot%20Noir%20Willamette%20Valley%20Eola-Amity%20Hills%20Jessie%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Cristom Pinot Noir Willamette Valley Eola-Amity Hills Jessie Vineyard",url:"https://www.jamessuckling.com/tasting-notes/156248/cristom-pinot-noir-willamette-valley-eola-amity-hills-jessie-vineyard-2018/?sid=397ec86755cddae1cbdcaa5c47e7f0c6"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-16">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-16" data-target="#collapse-16">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">16</span><span class="title-vintage">Thörle Spätburgunder Rheinhessen Hölle 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-16">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Rheinhessen</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Thörle Spätburgunder Rheinhessen Hölle/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This pinot noir masterpiece announces Rheinhessen’s arrival on the list of wine regions where this grape variety is capable of the highest sophistication. So deep and finely nuanced with ravishing sweetness that sweeps you off your feet. Then comes the enormously complex finish where the fine tannins build to a breathtaking crescendo. From organically grown grapes. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/161428/thorle-spatburgunder-rheinhessen-holle-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_16"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161428%2Fthorle-spatburgunder-rheinhessen-holle-2019%2F%3Fsid%3Dec4c5ec3d972c3910cd9d24fa606a7bf&amp;linkname=Th%C3%B6rle%20Sp%C3%A4tburgunder%20Rheinhessen%20H%C3%B6lle" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161428%2Fthorle-spatburgunder-rheinhessen-holle-2019%2F%3Fsid%3Dec4c5ec3d972c3910cd9d24fa606a7bf&amp;linkname=Th%C3%B6rle%20Sp%C3%A4tburgunder%20Rheinhessen%20H%C3%B6lle" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161428%2Fthorle-spatburgunder-rheinhessen-holle-2019%2F%3Fsid%3Dec4c5ec3d972c3910cd9d24fa606a7bf&amp;linkname=Th%C3%B6rle%20Sp%C3%A4tburgunder%20Rheinhessen%20H%C3%B6lle" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161428%2Fthorle-spatburgunder-rheinhessen-holle-2019%2F%3Fsid%3Dec4c5ec3d972c3910cd9d24fa606a7bf&amp;linkname=Th%C3%B6rle%20Sp%C3%A4tburgunder%20Rheinhessen%20H%C3%B6lle" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Th\u00f6rle Sp\u00e4tburgunder Rheinhessen H\u00f6lle",url:"https://www.jamessuckling.com/tasting-notes/161428/thorle-spatburgunder-rheinhessen-holle-2019/?sid=ec4c5ec3d972c3910cd9d24fa606a7bf"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-17">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-17" data-target="#collapse-17">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">17</span><span class="title-vintage">Emrich-Schönleber Riesling Nahe Halenberg GG 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-17">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Nahe</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Emrich-Schönleber Riesling Nahe Halenberg GG/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Enormously fine and subtle nose. The ravishing but very delicate apricot aroma pulls you into the profound mineral depths of this dry-riesling masterpiece. The salty minerality at the finish just doesn’t want to stop and gives you a great feeling of how the most dramatic landscapes of this region look. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/157939/emrich-schonleber-riesling-nahe-halenberg-gg-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_17"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157939%2Femrich-schonleber-riesling-nahe-halenberg-gg-2020%2F%3Fsid%3Db25b1d987243622f065f6bb5074d9c2b&amp;linkname=Emrich-Sch%C3%B6nleber%20Riesling%20Nahe%20Halenberg%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157939%2Femrich-schonleber-riesling-nahe-halenberg-gg-2020%2F%3Fsid%3Db25b1d987243622f065f6bb5074d9c2b&amp;linkname=Emrich-Sch%C3%B6nleber%20Riesling%20Nahe%20Halenberg%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157939%2Femrich-schonleber-riesling-nahe-halenberg-gg-2020%2F%3Fsid%3Db25b1d987243622f065f6bb5074d9c2b&amp;linkname=Emrich-Sch%C3%B6nleber%20Riesling%20Nahe%20Halenberg%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157939%2Femrich-schonleber-riesling-nahe-halenberg-gg-2020%2F%3Fsid%3Db25b1d987243622f065f6bb5074d9c2b&amp;linkname=Emrich-Sch%C3%B6nleber%20Riesling%20Nahe%20Halenberg%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Emrich-Sch\u00f6nleber Riesling Nahe Halenberg GG",url:"https://www.jamessuckling.com/tasting-notes/157939/emrich-schonleber-riesling-nahe-halenberg-gg-2020/?sid=b25b1d987243622f065f6bb5074d9c2b"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-18">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-18" data-target="#collapse-18">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">18</span><span class="title-vintage">F.X. Pichler Riesling Wachau Ried Kellerberg 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-18">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Austria</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Danube</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/F.X. Pichler Riesling Wachau Ried Kellerberg/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">You need some time to wrap your head around this mineral masterpiece. So pristine and delicate, in spite of the enormous concentration and stony power behind it. Yes, there are a ton of citrus, white-peach and wild-rose aromas in there, and yes, there are intense wild herbs, too, but these things only scratch the surface of its soul. What’s more, it only has 12.5% alcohol! Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/162868/f-x-pichler-riesling-wachau-ried-kellerberg-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_18"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162868%2Ff-x-pichler-riesling-wachau-ried-kellerberg-2020%2F%3Fsid%3D17679ef6b83db5421c1c1e925b1286ca&amp;linkname=F.X.%20Pichler%20Riesling%20Wachau%20Ried%20Kellerberg" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162868%2Ff-x-pichler-riesling-wachau-ried-kellerberg-2020%2F%3Fsid%3D17679ef6b83db5421c1c1e925b1286ca&amp;linkname=F.X.%20Pichler%20Riesling%20Wachau%20Ried%20Kellerberg" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162868%2Ff-x-pichler-riesling-wachau-ried-kellerberg-2020%2F%3Fsid%3D17679ef6b83db5421c1c1e925b1286ca&amp;linkname=F.X.%20Pichler%20Riesling%20Wachau%20Ried%20Kellerberg" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162868%2Ff-x-pichler-riesling-wachau-ried-kellerberg-2020%2F%3Fsid%3D17679ef6b83db5421c1c1e925b1286ca&amp;linkname=F.X.%20Pichler%20Riesling%20Wachau%20Ried%20Kellerberg" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"F.X. Pichler Riesling Wachau Ried Kellerberg",url:"https://www.jamessuckling.com/tasting-notes/162868/f-x-pichler-riesling-wachau-ried-kellerberg-2020/?sid=17679ef6b83db5421c1c1e925b1286ca"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-19">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-19" data-target="#collapse-19">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">19</span><span class="title-vintage">Lokoya Cabernet Sauvignon Napa Valley Mount Veeder 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-19">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Lokoya Cabernet Sauvignon Napa Valley Mount Veeder/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Blackberries, herbs, green pine needles, blackcurrants and lead pencil. Full-bodied with incredible structure and powerful tannins. It goes on for minutes. The structure is something else. Muscular, but the tannins give form and focus to the beautiful fruit. Mountain-grown Latour! Extraordinary. Try after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149468/lokoya-cabernet-sauvignon-napa-valley-mount-veeder-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_19"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149468%2Flokoya-cabernet-sauvignon-napa-valley-mount-veeder-2018%2F%3Fsid%3D673e68c11ed1dfe6402a82d1c64b1cc0&amp;linkname=Lokoya%20Cabernet%20Sauvignon%20Napa%20Valley%20Mount%20Veeder" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149468%2Flokoya-cabernet-sauvignon-napa-valley-mount-veeder-2018%2F%3Fsid%3D673e68c11ed1dfe6402a82d1c64b1cc0&amp;linkname=Lokoya%20Cabernet%20Sauvignon%20Napa%20Valley%20Mount%20Veeder" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149468%2Flokoya-cabernet-sauvignon-napa-valley-mount-veeder-2018%2F%3Fsid%3D673e68c11ed1dfe6402a82d1c64b1cc0&amp;linkname=Lokoya%20Cabernet%20Sauvignon%20Napa%20Valley%20Mount%20Veeder" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149468%2Flokoya-cabernet-sauvignon-napa-valley-mount-veeder-2018%2F%3Fsid%3D673e68c11ed1dfe6402a82d1c64b1cc0&amp;linkname=Lokoya%20Cabernet%20Sauvignon%20Napa%20Valley%20Mount%20Veeder" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Lokoya Cabernet Sauvignon Napa Valley Mount Veeder",url:"https://www.jamessuckling.com/tasting-notes/149468/lokoya-cabernet-sauvignon-napa-valley-mount-veeder-2018/?sid=673e68c11ed1dfe6402a82d1c64b1cc0"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-20">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-20" data-target="#collapse-20">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">20</span><span class="title-vintage">Foradori Manzoni Bianco Vigneti delle Dolomiti Fontanasanta 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-20">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Northeast</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Foradori Manzoni Bianco Vigneti delle Dolomiti Fontanasanta/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Maybe the greatest natural white wine I have ever tasted. Complex and strikingly original lemon-zest, smoke and dried-chamomile aromas pour from the glass. Then comes the concentrated but very refined palate,followed by a super-long finish that’s a cascading waterfall of wet-stone minerality. Just doesn’t want to stop! From biodynamically grown grapes with Demeter certification. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/151251/foradori-manzoni-bianco-vigneti-delle-dolomiti-fontanasanta-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_20"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151251%2Fforadori-manzoni-bianco-vigneti-delle-dolomiti-fontanasanta-2020%2F%3Fsid%3D982cad476caa2b030ba736c3cbcf1dec&amp;linkname=Foradori%20Manzoni%20Bianco%20Vigneti%20delle%20Dolomiti%20Fontanasanta" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151251%2Fforadori-manzoni-bianco-vigneti-delle-dolomiti-fontanasanta-2020%2F%3Fsid%3D982cad476caa2b030ba736c3cbcf1dec&amp;linkname=Foradori%20Manzoni%20Bianco%20Vigneti%20delle%20Dolomiti%20Fontanasanta" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151251%2Fforadori-manzoni-bianco-vigneti-delle-dolomiti-fontanasanta-2020%2F%3Fsid%3D982cad476caa2b030ba736c3cbcf1dec&amp;linkname=Foradori%20Manzoni%20Bianco%20Vigneti%20delle%20Dolomiti%20Fontanasanta" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151251%2Fforadori-manzoni-bianco-vigneti-delle-dolomiti-fontanasanta-2020%2F%3Fsid%3D982cad476caa2b030ba736c3cbcf1dec&amp;linkname=Foradori%20Manzoni%20Bianco%20Vigneti%20delle%20Dolomiti%20Fontanasanta" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Foradori Manzoni Bianco Vigneti delle Dolomiti Fontanasanta",url:"https://www.jamessuckling.com/tasting-notes/151251/foradori-manzoni-bianco-vigneti-delle-dolomiti-fontanasanta-2020/?sid=982cad476caa2b030ba736c3cbcf1dec"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-21">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-21" data-target="#collapse-21">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">21</span><span class="title-vintage">Moric Blaufränkisch Burgenland Lutzmannsburg Alte Reben 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-21">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Austria</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Burgenland</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Moric Blaufränkisch Burgenland Lutzmannsburg Alte Reben/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Although this is already fragrant, the bouquet only hints at the enormous depth of this super-elegant blaufrankisch red. So graceful and refined, it redefines what the red wines of this grape can be. The giant structure is buried underneath a mountain of ripeness. Then the finish hits you like a lightning strike. Enormous aging potential. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/162869/moric-blaufrankisch-burgenland-lutzmannsburg-alte-reben-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_21"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162869%2Fmoric-blaufrankisch-burgenland-lutzmannsburg-alte-reben-2019%2F%3Fsid%3D242bac7e0c26da8b76e53d1da5986f86&amp;linkname=Moric%20Blaufr%C3%A4nkisch%20Burgenland%20Lutzmannsburg%20Alte%20Reben" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162869%2Fmoric-blaufrankisch-burgenland-lutzmannsburg-alte-reben-2019%2F%3Fsid%3D242bac7e0c26da8b76e53d1da5986f86&amp;linkname=Moric%20Blaufr%C3%A4nkisch%20Burgenland%20Lutzmannsburg%20Alte%20Reben" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162869%2Fmoric-blaufrankisch-burgenland-lutzmannsburg-alte-reben-2019%2F%3Fsid%3D242bac7e0c26da8b76e53d1da5986f86&amp;linkname=Moric%20Blaufr%C3%A4nkisch%20Burgenland%20Lutzmannsburg%20Alte%20Reben" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162869%2Fmoric-blaufrankisch-burgenland-lutzmannsburg-alte-reben-2019%2F%3Fsid%3D242bac7e0c26da8b76e53d1da5986f86&amp;linkname=Moric%20Blaufr%C3%A4nkisch%20Burgenland%20Lutzmannsburg%20Alte%20Reben" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Moric Blaufr\u00e4nkisch Burgenland Lutzmannsburg Alte Reben",url:"https://www.jamessuckling.com/tasting-notes/162869/moric-blaufrankisch-burgenland-lutzmannsburg-alte-reben-2019/?sid=242bac7e0c26da8b76e53d1da5986f86"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-22">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-22" data-target="#collapse-22">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">22</span><span class="title-vintage">Tenuta Sette Ponti Toscana Oreno 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-22">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Tenuta Sette Ponti Toscana Oreno/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Wow. Fantastic aromas of blackberries, currants, minerals, violets and graphite. Full-bodied with firm, silky tannins that are incredibly polished and intense, yet ever so refined and integrated in the wine. It goes on for minutes. The is one of the best modern-day Orenos so far. Best in 2025 and onwards.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/156895/tenuta-sette-ponti-toscana-oreno-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_22"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156895%2Ftenuta-sette-ponti-toscana-oreno-2019%2F%3Fsid%3Dfe09c34892ee3a072935aa687c391038&amp;linkname=Tenuta%20Sette%20Ponti%20Toscana%20Oreno" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156895%2Ftenuta-sette-ponti-toscana-oreno-2019%2F%3Fsid%3Dfe09c34892ee3a072935aa687c391038&amp;linkname=Tenuta%20Sette%20Ponti%20Toscana%20Oreno" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156895%2Ftenuta-sette-ponti-toscana-oreno-2019%2F%3Fsid%3Dfe09c34892ee3a072935aa687c391038&amp;linkname=Tenuta%20Sette%20Ponti%20Toscana%20Oreno" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F156895%2Ftenuta-sette-ponti-toscana-oreno-2019%2F%3Fsid%3Dfe09c34892ee3a072935aa687c391038&amp;linkname=Tenuta%20Sette%20Ponti%20Toscana%20Oreno" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Tenuta Sette Ponti Toscana Oreno",url:"https://www.jamessuckling.com/tasting-notes/156895/tenuta-sette-ponti-toscana-oreno-2019/?sid=fe09c34892ee3a072935aa687c391038"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-23">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-23" data-target="#collapse-23">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">23</span><span class="title-vintage">Künstler Riesling Rheingau Hölle GG 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-23">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Rheingau</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Künstler Riesling Rheingau Hölle GG/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">The deep, peach and apricot nose leads you into this enormously concentrated yet graceful dry riesling that’s got the stature to stand next to almost any Grand Cru white Burgundy. Enormously long, beautifully balanced finish that pulls your hand magnetically back to the glass. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/162196/kunstler-riesling-rheingau-holle-gg-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_23"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162196%2Fkunstler-riesling-rheingau-holle-gg-2020%2F%3Fsid%3D3b0043e2cbde4ad10b63b0c401e0fd87&amp;linkname=K%C3%BCnstler%20Riesling%20Rheingau%20H%C3%B6lle%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162196%2Fkunstler-riesling-rheingau-holle-gg-2020%2F%3Fsid%3D3b0043e2cbde4ad10b63b0c401e0fd87&amp;linkname=K%C3%BCnstler%20Riesling%20Rheingau%20H%C3%B6lle%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162196%2Fkunstler-riesling-rheingau-holle-gg-2020%2F%3Fsid%3D3b0043e2cbde4ad10b63b0c401e0fd87&amp;linkname=K%C3%BCnstler%20Riesling%20Rheingau%20H%C3%B6lle%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162196%2Fkunstler-riesling-rheingau-holle-gg-2020%2F%3Fsid%3D3b0043e2cbde4ad10b63b0c401e0fd87&amp;linkname=K%C3%BCnstler%20Riesling%20Rheingau%20H%C3%B6lle%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"K\u00fcnstler Riesling Rheingau H\u00f6lle GG",url:"https://www.jamessuckling.com/tasting-notes/162196/kunstler-riesling-rheingau-holle-gg-2020/?sid=3b0043e2cbde4ad10b63b0c401e0fd87"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-24">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-24" data-target="#collapse-24">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">24</span><span class="title-vintage">Fattoria Le Pupille Maremma Toscana Saffredi  2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-24">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Fattoria Le Pupille Maremma Toscana Saffredi /2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">So much crushed stone, rosemary, lavender, mint and blackberry. Full-bodied and very structured with layers of powerful and polished tannins. It goes on for minutes. Ink, blackcurrants and blueberries. 60% cabernet sauvignon, 35% merlot and 5% petit verdot. Needs at least five or six years to open. Try after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/164506/fattoria-le-pupille-maremma-toscana-saffredi-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_24"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164506%2Ffattoria-le-pupille-maremma-toscana-saffredi-2019%2F%3Fsid%3D8cc2f5fbfccf17fe954a9cf6ce84baf2&amp;linkname=Fattoria%20Le%20Pupille%20Maremma%20Toscana%20Saffredi%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164506%2Ffattoria-le-pupille-maremma-toscana-saffredi-2019%2F%3Fsid%3D8cc2f5fbfccf17fe954a9cf6ce84baf2&amp;linkname=Fattoria%20Le%20Pupille%20Maremma%20Toscana%20Saffredi%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164506%2Ffattoria-le-pupille-maremma-toscana-saffredi-2019%2F%3Fsid%3D8cc2f5fbfccf17fe954a9cf6ce84baf2&amp;linkname=Fattoria%20Le%20Pupille%20Maremma%20Toscana%20Saffredi%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164506%2Ffattoria-le-pupille-maremma-toscana-saffredi-2019%2F%3Fsid%3D8cc2f5fbfccf17fe954a9cf6ce84baf2&amp;linkname=Fattoria%20Le%20Pupille%20Maremma%20Toscana%20Saffredi%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Fattoria Le Pupille Maremma Toscana Saffredi ",url:"https://www.jamessuckling.com/tasting-notes/164506/fattoria-le-pupille-maremma-toscana-saffredi-2019/?sid=8cc2f5fbfccf17fe954a9cf6ce84baf2"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-25">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-25" data-target="#collapse-25">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">25</span><span class="title-vintage">Domaine de Chevalier Pessac-Léognan 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-25">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Domaine de Chevalier Pessac-Léognan/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">The intensity and perfumes on the nose are extremely impressive, offering pure blackberries and violets, as well as bark, wild-mushroom and raw-tile notes. It’s full-bodied with creamy tannins that envelop the wine and a gorgeous, subtly complex center palate with all the flavors found on the nose. Endless finish. Love the finesse and length to this. Greatest ever. 65% cabernet sauvignon, 30% merlot and 5% petit verdot. Try after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145529/domaine-de-chevalier-pessac-leognan-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_25"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145529%2Fdomaine-de-chevalier-pessac-leognan-2018%2F%3Fsid%3D5185112b3e062b6d47a6104328a4de4f&amp;linkname=Domaine%20de%20Chevalier%20Pessac-L%C3%A9ognan" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145529%2Fdomaine-de-chevalier-pessac-leognan-2018%2F%3Fsid%3D5185112b3e062b6d47a6104328a4de4f&amp;linkname=Domaine%20de%20Chevalier%20Pessac-L%C3%A9ognan" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145529%2Fdomaine-de-chevalier-pessac-leognan-2018%2F%3Fsid%3D5185112b3e062b6d47a6104328a4de4f&amp;linkname=Domaine%20de%20Chevalier%20Pessac-L%C3%A9ognan" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145529%2Fdomaine-de-chevalier-pessac-leognan-2018%2F%3Fsid%3D5185112b3e062b6d47a6104328a4de4f&amp;linkname=Domaine%20de%20Chevalier%20Pessac-L%C3%A9ognan" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Domaine de Chevalier Pessac-L\u00e9ognan",url:"https://www.jamessuckling.com/tasting-notes/145529/domaine-de-chevalier-pessac-leognan-2018/?sid=5185112b3e062b6d47a6104328a4de4f"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-26">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-26" data-target="#collapse-26">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">26</span><span class="title-vintage">Adelina Shiraz Clare Valley 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-26">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">South Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Adelina Shiraz Clare Valley/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">From a low-yielding vintage that was warm enough, yet also cool enough, this is an exceptional release of what is fast becoming one of the great wines of not only the Clare Valley, but of South Australia. Some depth to the color and plenty of blueberry, red-plum and wild-raspberry aromas. The nose is so pure and attractive. With assertive tannin, as you’d expect here, the palate is framed up handsomely and the concentrated red-plum, raspberry, blueberry and blackberry flavors hold seamless and fresh. Vivid clarity here. Stunning. Try from 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/154557/adelina-shiraz-clare-valley-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_26"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154557%2Fadelina-shiraz-clare-valley-2020%2F%3Fsid%3D4793f7942f340d523ec6c50c94a14e25&amp;linkname=Adelina%20Shiraz%20Clare%20Valley" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154557%2Fadelina-shiraz-clare-valley-2020%2F%3Fsid%3D4793f7942f340d523ec6c50c94a14e25&amp;linkname=Adelina%20Shiraz%20Clare%20Valley" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154557%2Fadelina-shiraz-clare-valley-2020%2F%3Fsid%3D4793f7942f340d523ec6c50c94a14e25&amp;linkname=Adelina%20Shiraz%20Clare%20Valley" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154557%2Fadelina-shiraz-clare-valley-2020%2F%3Fsid%3D4793f7942f340d523ec6c50c94a14e25&amp;linkname=Adelina%20Shiraz%20Clare%20Valley" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Adelina Shiraz Clare Valley",url:"https://www.jamessuckling.com/tasting-notes/154557/adelina-shiraz-clare-valley-2020/?sid=4793f7942f340d523ec6c50c94a14e25"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-27">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-27" data-target="#collapse-27">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">27</span><span class="title-vintage">Casanova di Neri Brunello di Montalcino Cerretalto 2016</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-27">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2016</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Casanova di Neri Brunello di Montalcino Cerretalto/2016/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Wow. Incredible purity and transparency with cherries, bark, mushroom, flower and slate/stone on the nose. Full-bodied yet agile and fresh with a fine tannin structure that runs the length of the wine and goes on forever. The polish, elegance and grace is breathtaking. Power with agility. A revelation for the 2016 vintage in Brunello. Drink in 2024 and onwards but wonderful to taste now.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/167171/casanova-di-neri-brunello-di-montalcino-cerretalto-2016">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_27"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167171%2Fcasanova-di-neri-brunello-di-montalcino-cerretalto-2016%2F%3Fsid%3D5b300df72a8eeb781710617da4502ddb&amp;linkname=Casanova%20di%20Neri%20Brunello%20di%20Montalcino%20Cerretalto" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167171%2Fcasanova-di-neri-brunello-di-montalcino-cerretalto-2016%2F%3Fsid%3D5b300df72a8eeb781710617da4502ddb&amp;linkname=Casanova%20di%20Neri%20Brunello%20di%20Montalcino%20Cerretalto" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167171%2Fcasanova-di-neri-brunello-di-montalcino-cerretalto-2016%2F%3Fsid%3D5b300df72a8eeb781710617da4502ddb&amp;linkname=Casanova%20di%20Neri%20Brunello%20di%20Montalcino%20Cerretalto" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167171%2Fcasanova-di-neri-brunello-di-montalcino-cerretalto-2016%2F%3Fsid%3D5b300df72a8eeb781710617da4502ddb&amp;linkname=Casanova%20di%20Neri%20Brunello%20di%20Montalcino%20Cerretalto" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Casanova di Neri Brunello di Montalcino Cerretalto",url:"https://www.jamessuckling.com/tasting-notes/167171/casanova-di-neri-brunello-di-montalcino-cerretalto-2016/?sid=5b300df72a8eeb781710617da4502ddb"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-28">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-28" data-target="#collapse-28">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">28</span><span class="title-vintage">Domaine Weinbach Riesling Alsace Grand Cru Schlossberg Cuvée Ste. Catherine 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-28">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Alsace</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Domaine Weinbach Riesling Alsace Grand Cru Schlossberg Cuvée Ste. Catherine/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Enveloping, sensual bouquet of a thousand yellow fruits and some wild berries that’s just beginning to reveal its profundity. Gigantic concentration, but this remains as light on its feet as a prima ballerina. The gentle creaminess on the palate perfectly balances the mineral acidity that seems to blink like a star low in the sky. Enormously long and subtle finish. From biodynamically grown grapes with Demeter certification. Drinkable now, but better from 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/155127/domaine-weinbach-riesling-alsace-grand-cru-schlossberg-cuvee-ste-catherine-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_28"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155127%2Fdomaine-weinbach-riesling-alsace-grand-cru-schlossberg-cuvee-ste-catherine-2019%2F%3Fsid%3Df0bebe5cc9ba7fed0b6326d452a178eb&amp;linkname=Domaine%20Weinbach%20Riesling%20Alsace%20Grand%20Cru%20Schlossberg%20Cuv%C3%A9e%20Ste.%20Catherine" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155127%2Fdomaine-weinbach-riesling-alsace-grand-cru-schlossberg-cuvee-ste-catherine-2019%2F%3Fsid%3Df0bebe5cc9ba7fed0b6326d452a178eb&amp;linkname=Domaine%20Weinbach%20Riesling%20Alsace%20Grand%20Cru%20Schlossberg%20Cuv%C3%A9e%20Ste.%20Catherine" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155127%2Fdomaine-weinbach-riesling-alsace-grand-cru-schlossberg-cuvee-ste-catherine-2019%2F%3Fsid%3Df0bebe5cc9ba7fed0b6326d452a178eb&amp;linkname=Domaine%20Weinbach%20Riesling%20Alsace%20Grand%20Cru%20Schlossberg%20Cuv%C3%A9e%20Ste.%20Catherine" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155127%2Fdomaine-weinbach-riesling-alsace-grand-cru-schlossberg-cuvee-ste-catherine-2019%2F%3Fsid%3Df0bebe5cc9ba7fed0b6326d452a178eb&amp;linkname=Domaine%20Weinbach%20Riesling%20Alsace%20Grand%20Cru%20Schlossberg%20Cuv%C3%A9e%20Ste.%20Catherine" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Domaine Weinbach Riesling Alsace Grand Cru Schlossberg Cuv\u00e9e Ste. Catherine",url:"https://www.jamessuckling.com/tasting-notes/155127/domaine-weinbach-riesling-alsace-grand-cru-schlossberg-cuvee-ste-catherine-2019/?sid=f0bebe5cc9ba7fed0b6326d452a178eb"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-29">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-29" data-target="#collapse-29">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">29</span><span class="title-vintage">Realm Cellars Napa Valley Stags Leap District Moonracer 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-29">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Realm Cellars Napa Valley Stags Leap District Moonracer/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A full-bodied, structured red with blackcurrant, violet, dark-chocolate and burnt-orange aromas. Walnut husk, too. Such precision and elegance. Firm, smooth tannins and a long finish. Really complex at the end. A stunning wine from Stags Leap District. Drink from 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/143426/realm-cellars-napa-valley-stags-leap-district-moonracer-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_29"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F143426%2Frealm-cellars-napa-valley-stags-leap-district-moonracer-2018%2F%3Fsid%3Dae7af9cd31bba5aa32501e5683d07b29&amp;linkname=Realm%20Cellars%20Napa%20Valley%20Stags%20Leap%20District%20Moonracer" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F143426%2Frealm-cellars-napa-valley-stags-leap-district-moonracer-2018%2F%3Fsid%3Dae7af9cd31bba5aa32501e5683d07b29&amp;linkname=Realm%20Cellars%20Napa%20Valley%20Stags%20Leap%20District%20Moonracer" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F143426%2Frealm-cellars-napa-valley-stags-leap-district-moonracer-2018%2F%3Fsid%3Dae7af9cd31bba5aa32501e5683d07b29&amp;linkname=Realm%20Cellars%20Napa%20Valley%20Stags%20Leap%20District%20Moonracer" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F143426%2Frealm-cellars-napa-valley-stags-leap-district-moonracer-2018%2F%3Fsid%3Dae7af9cd31bba5aa32501e5683d07b29&amp;linkname=Realm%20Cellars%20Napa%20Valley%20Stags%20Leap%20District%20Moonracer" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Realm Cellars Napa Valley Stags Leap District Moonracer",url:"https://www.jamessuckling.com/tasting-notes/143426/realm-cellars-napa-valley-stags-leap-district-moonracer-2018/?sid=ae7af9cd31bba5aa32501e5683d07b29"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-30">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-30" data-target="#collapse-30">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">30</span><span class="title-vintage">Bouchard Père &amp; Fils Chevalier-Montrachet Grand Cru Domaine 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-30">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Burgundy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Bouchard Père &amp; Fils Chevalier-Montrachet Grand Cru Domaine/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Its really hard to imagine how a white Brugundy could be more flinty and minerally than this super-concentrated and super-vibrant Chevalier Montrachet. Lovely aromas of lemon blossom, jasmine, tangerine and nectarine, alongside all the stony stuff. Then comes the staggeringly long finish that is totally pure and precise. From Bouchard’s 2.3-hectare holding, which comprises almost a third of the entire Grand Cru site. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/158504/bouchard-pere-fils-chevalier-montrachet-grand-cru-domaine-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_30"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158504%2Fbouchard-pere-fils-chevalier-montrachet-grand-cru-domaine-2019%2F%3Fsid%3D5a70a3d453781f07bbe10116f9025538&amp;linkname=Bouchard%20P%C3%A8re%20%26%20Fils%20Chevalier-Montrachet%20Grand%20Cru%20Domaine" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158504%2Fbouchard-pere-fils-chevalier-montrachet-grand-cru-domaine-2019%2F%3Fsid%3D5a70a3d453781f07bbe10116f9025538&amp;linkname=Bouchard%20P%C3%A8re%20%26%20Fils%20Chevalier-Montrachet%20Grand%20Cru%20Domaine" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158504%2Fbouchard-pere-fils-chevalier-montrachet-grand-cru-domaine-2019%2F%3Fsid%3D5a70a3d453781f07bbe10116f9025538&amp;linkname=Bouchard%20P%C3%A8re%20%26%20Fils%20Chevalier-Montrachet%20Grand%20Cru%20Domaine" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158504%2Fbouchard-pere-fils-chevalier-montrachet-grand-cru-domaine-2019%2F%3Fsid%3D5a70a3d453781f07bbe10116f9025538&amp;linkname=Bouchard%20P%C3%A8re%20%26%20Fils%20Chevalier-Montrachet%20Grand%20Cru%20Domaine" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Bouchard P\u00e8re & Fils Chevalier-Montrachet Grand Cru Domaine",url:"https://www.jamessuckling.com/tasting-notes/158504/bouchard-pere-fils-chevalier-montrachet-grand-cru-domaine-2019/?sid=5a70a3d453781f07bbe10116f9025538"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-31">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-31" data-target="#collapse-31">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">31</span><span class="title-vintage">Krug Champagne Brut 2008</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-31">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Champagne</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2008</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Krug Champagne Brut/2008/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is very structured and framed with an almost red sensibility. Very phenolic. Full-bodied in a tightly wound ball with so much going on. Very pinot like. Mineral and stone. Shell and stone. Iodine. Vinous. The bubbles just fade into the finish of the wine, which goes on for minutes. Turns to toffee and salted caramel with time in the glass. One for the cellar. Great length. Blend of 53% pinot noir, 25% pinot meunier, 22% chardonnay. Disgorged in beginning of 2020. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/167172/krug-champagne-brut-2008">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_31"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167172%2Fkrug-champagne-brut-2008%2F%3Fsid%3De8da9fe4864d829c48cdf144a768b4ad&amp;linkname=Krug%20Champagne%20Brut" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167172%2Fkrug-champagne-brut-2008%2F%3Fsid%3De8da9fe4864d829c48cdf144a768b4ad&amp;linkname=Krug%20Champagne%20Brut" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167172%2Fkrug-champagne-brut-2008%2F%3Fsid%3De8da9fe4864d829c48cdf144a768b4ad&amp;linkname=Krug%20Champagne%20Brut" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167172%2Fkrug-champagne-brut-2008%2F%3Fsid%3De8da9fe4864d829c48cdf144a768b4ad&amp;linkname=Krug%20Champagne%20Brut" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Krug Champagne Brut",url:"https://www.jamessuckling.com/tasting-notes/167172/krug-champagne-brut-2008/?sid=e8da9fe4864d829c48cdf144a768b4ad"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-32">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-32" data-target="#collapse-32">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">32</span><span class="title-vintage">Ciacci Piccolomini d'Aragona Brunello di Montalcino Vigna di Pianrosso Santa Caterina d'Oro Riserva 2016</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-32">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2016</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Ciacci Piccolomini d'Aragona Brunello di Montalcino Vigna di Pianrosso Santa Caterina d'Oro Riserva/2016/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Glorious aromas of flowers, nutmeg, dark berries, earth and black cherries follow through to a full body with ultra-fine tannins that are long and extremely polished. They go on for minutes. Reserved and shy still, due to its excellence. Give this four or five years to come around. Try after 2024.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/165081/ciacci-piccolomini-daragona-brunello-di-montalcino-vigna-di-pianrosso-santa-caterina-doro-riserva-2016">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_32"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165081%2Fciacci-piccolomini-daragona-brunello-di-montalcino-vigna-di-pianrosso-santa-caterina-doro-riserva-2016%2F%3Fsid%3Dbe80102f13aa91cb5c705f55106e5a0b&amp;linkname=Ciacci%20Piccolomini%20d%27Aragona%20Brunello%20di%20Montalcino%20Vigna%20di%20Pianrosso%20Santa%20Caterina%20d%27Oro%20Riserva" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165081%2Fciacci-piccolomini-daragona-brunello-di-montalcino-vigna-di-pianrosso-santa-caterina-doro-riserva-2016%2F%3Fsid%3Dbe80102f13aa91cb5c705f55106e5a0b&amp;linkname=Ciacci%20Piccolomini%20d%27Aragona%20Brunello%20di%20Montalcino%20Vigna%20di%20Pianrosso%20Santa%20Caterina%20d%27Oro%20Riserva" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165081%2Fciacci-piccolomini-daragona-brunello-di-montalcino-vigna-di-pianrosso-santa-caterina-doro-riserva-2016%2F%3Fsid%3Dbe80102f13aa91cb5c705f55106e5a0b&amp;linkname=Ciacci%20Piccolomini%20d%27Aragona%20Brunello%20di%20Montalcino%20Vigna%20di%20Pianrosso%20Santa%20Caterina%20d%27Oro%20Riserva" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165081%2Fciacci-piccolomini-daragona-brunello-di-montalcino-vigna-di-pianrosso-santa-caterina-doro-riserva-2016%2F%3Fsid%3Dbe80102f13aa91cb5c705f55106e5a0b&amp;linkname=Ciacci%20Piccolomini%20d%27Aragona%20Brunello%20di%20Montalcino%20Vigna%20di%20Pianrosso%20Santa%20Caterina%20d%27Oro%20Riserva" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ciacci Piccolomini d'Aragona Brunello di Montalcino Vigna di Pianrosso Santa Caterina d'Oro Riserva",url:"https://www.jamessuckling.com/tasting-notes/165081/ciacci-piccolomini-daragona-brunello-di-montalcino-vigna-di-pianrosso-santa-caterina-doro-riserva-2016/?sid=be80102f13aa91cb5c705f55106e5a0b"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-33">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-33" data-target="#collapse-33">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">33</span><span class="title-vintage">Leitz Riesling Rheingau Berg Schlossberg GG 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-33">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Rheingau</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Leitz Riesling Rheingau Berg Schlossberg GG/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A towering giant of peach, apricot and King Alfonso mango aromas that opens slowly like a rose. Great juiciness, but of the most refined kind. Stunning interplay of fruit and minerality right through the very long, pristine finish. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/159882/leitz-riesling-rheingau-berg-schlossberg-gg-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_33"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159882%2Fleitz-riesling-rheingau-berg-schlossberg-gg-2019%2F%3Fsid%3D563fde884ee60e999b90ec1fa7b2358e&amp;linkname=Leitz%20Riesling%20Rheingau%20Berg%20Schlossberg%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159882%2Fleitz-riesling-rheingau-berg-schlossberg-gg-2019%2F%3Fsid%3D563fde884ee60e999b90ec1fa7b2358e&amp;linkname=Leitz%20Riesling%20Rheingau%20Berg%20Schlossberg%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159882%2Fleitz-riesling-rheingau-berg-schlossberg-gg-2019%2F%3Fsid%3D563fde884ee60e999b90ec1fa7b2358e&amp;linkname=Leitz%20Riesling%20Rheingau%20Berg%20Schlossberg%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159882%2Fleitz-riesling-rheingau-berg-schlossberg-gg-2019%2F%3Fsid%3D563fde884ee60e999b90ec1fa7b2358e&amp;linkname=Leitz%20Riesling%20Rheingau%20Berg%20Schlossberg%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Leitz Riesling Rheingau Berg Schlossberg GG",url:"https://www.jamessuckling.com/tasting-notes/159882/leitz-riesling-rheingau-berg-schlossberg-gg-2019/?sid=563fde884ee60e999b90ec1fa7b2358e"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-34">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-34" data-target="#collapse-34">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">34</span><span class="title-vintage">Château Haut-Bailly Pessac-Léognan 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-34">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Haut-Bailly Pessac-Léognan/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Complex and expressive nose, offering red and dark fruit, spices and pepper with wood and mushroom undertones. Fresh mussel shell and a hint of ink, too. Full-bodied with a fine texture and great balance between the acidity and the controlled, tannic structure. Very long finish. Goes on and on. Tiny production, 21 hectoliters per hectare. Try after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/144650/chateau-haut-bailly-pessac-leognan-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_34"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144650%2Fchateau-haut-bailly-pessac-leognan-2018%2F%3Fsid%3D74d003a26c33b1c17a02ee55a2f163dc&amp;linkname=Ch%C3%A2teau%20Haut-Bailly%20Pessac-L%C3%A9ognan" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144650%2Fchateau-haut-bailly-pessac-leognan-2018%2F%3Fsid%3D74d003a26c33b1c17a02ee55a2f163dc&amp;linkname=Ch%C3%A2teau%20Haut-Bailly%20Pessac-L%C3%A9ognan" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144650%2Fchateau-haut-bailly-pessac-leognan-2018%2F%3Fsid%3D74d003a26c33b1c17a02ee55a2f163dc&amp;linkname=Ch%C3%A2teau%20Haut-Bailly%20Pessac-L%C3%A9ognan" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144650%2Fchateau-haut-bailly-pessac-leognan-2018%2F%3Fsid%3D74d003a26c33b1c17a02ee55a2f163dc&amp;linkname=Ch%C3%A2teau%20Haut-Bailly%20Pessac-L%C3%A9ognan" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Haut-Bailly Pessac-L\u00e9ognan",url:"https://www.jamessuckling.com/tasting-notes/144650/chateau-haut-bailly-pessac-leognan-2018/?sid=74d003a26c33b1c17a02ee55a2f163dc"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-35">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-35" data-target="#collapse-35">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">35</span><span class="title-vintage">RAEN Pinot Noir Sonoma Coast Fort Ross-Seaview Sea Field Vineyard 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-35">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/RAEN Pinot Noir Sonoma Coast Fort Ross-Seaview Sea Field Vineyard/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is really refined with black tea, rose petals, orange and blue fruit. It’s medium-bodied with wild-strawberry and forest-floor flavors. Medium-bodied with great vibrancy and beautiful tannins running through the center palate, which is stitched into the wine. Long and true. 100% whole-cluster fermentation. Subtle and energetic. Better after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/153458/raen-pinot-noir-sonoma-coast-fort-ross-seaview-sea-field-vineyard-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_35"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153458%2Fraen-pinot-noir-sonoma-coast-fort-ross-seaview-sea-field-vineyard-2019%2F%3Fsid%3D5971e4b0f29c7e0eb9162f8bd3c1a4b3&amp;linkname=RAEN%20Pinot%20Noir%20Sonoma%20Coast%20Fort%20Ross-Seaview%20Sea%20Field%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153458%2Fraen-pinot-noir-sonoma-coast-fort-ross-seaview-sea-field-vineyard-2019%2F%3Fsid%3D5971e4b0f29c7e0eb9162f8bd3c1a4b3&amp;linkname=RAEN%20Pinot%20Noir%20Sonoma%20Coast%20Fort%20Ross-Seaview%20Sea%20Field%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153458%2Fraen-pinot-noir-sonoma-coast-fort-ross-seaview-sea-field-vineyard-2019%2F%3Fsid%3D5971e4b0f29c7e0eb9162f8bd3c1a4b3&amp;linkname=RAEN%20Pinot%20Noir%20Sonoma%20Coast%20Fort%20Ross-Seaview%20Sea%20Field%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153458%2Fraen-pinot-noir-sonoma-coast-fort-ross-seaview-sea-field-vineyard-2019%2F%3Fsid%3D5971e4b0f29c7e0eb9162f8bd3c1a4b3&amp;linkname=RAEN%20Pinot%20Noir%20Sonoma%20Coast%20Fort%20Ross-Seaview%20Sea%20Field%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"RAEN Pinot Noir Sonoma Coast Fort Ross-Seaview Sea Field Vineyard",url:"https://www.jamessuckling.com/tasting-notes/153458/raen-pinot-noir-sonoma-coast-fort-ross-seaview-sea-field-vineyard-2019/?sid=5971e4b0f29c7e0eb9162f8bd3c1a4b3"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-36">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix" data-toggle="collapse" data-parent="#accordion-36" data-target="#collapse-36" aria-expanded="true">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">36</span><span class="title-vintage">Château Mouton Rothschild Pauillac 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse in" id="collapse-36" aria-expanded="true" style="">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Mouton Rothschild Pauillac/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Exquisite purity of blackcurrants, raspberries and some citrus. The aromas flow from the glass. Full-bodied with seamless tannins that coat the palate and then fall into the center, to deliver a thoroughly refined and harmonious young red. Endless finish. 86% cabernet sauvignon. This is the new 1959, one of the legendary vintages of Mouton. Try after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145523/chateau-mouton-rothschild-pauillac-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_36"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145523%2Fchateau-mouton-rothschild-pauillac-2018%2F%3Fsid%3D41dd7638a32648359d2af647dbb7851a&amp;linkname=Ch%C3%A2teau%20Mouton%20Rothschild%20Pauillac" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145523%2Fchateau-mouton-rothschild-pauillac-2018%2F%3Fsid%3D41dd7638a32648359d2af647dbb7851a&amp;linkname=Ch%C3%A2teau%20Mouton%20Rothschild%20Pauillac" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145523%2Fchateau-mouton-rothschild-pauillac-2018%2F%3Fsid%3D41dd7638a32648359d2af647dbb7851a&amp;linkname=Ch%C3%A2teau%20Mouton%20Rothschild%20Pauillac" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145523%2Fchateau-mouton-rothschild-pauillac-2018%2F%3Fsid%3D41dd7638a32648359d2af647dbb7851a&amp;linkname=Ch%C3%A2teau%20Mouton%20Rothschild%20Pauillac" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Mouton Rothschild Pauillac",url:"https://www.jamessuckling.com/tasting-notes/145523/chateau-mouton-rothschild-pauillac-2018/?sid=41dd7638a32648359d2af647dbb7851a"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-37">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix" data-toggle="collapse" data-parent="#accordion-37" data-target="#collapse-37" aria-expanded="true">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">37</span><span class="title-vintage">Littorai Pinot Noir Sonoma County Sonoma Coast The Haven Vineyard 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse in" id="collapse-37" aria-expanded="true" style="">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Littorai Pinot Noir Sonoma County Sonoma Coast The Haven Vineyard/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A mix of juicy red and black berries and earthy, woody spice on the nose. Medium-bodied with such depth, balance and precision. Succulent black fruit and ripe red berries are carried by fine tannins, along with fresh mint, pine and dried roses. Fine-tuned precision and refinement. Phenomenal wine. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/167588/littorai-pinot-noir-sonoma-county-sonoma-coast-the-haven-vineyard-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_37"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167588%2Flittorai-pinot-noir-sonoma-county-sonoma-coast-the-haven-vineyard-2019%2F%3Fsid%3De5cf98cbdba74cf5423d1d7cd96ca5f5&amp;linkname=Littorai%20Pinot%20Noir%20Sonoma%20County%20Sonoma%20Coast%20The%20Haven%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167588%2Flittorai-pinot-noir-sonoma-county-sonoma-coast-the-haven-vineyard-2019%2F%3Fsid%3De5cf98cbdba74cf5423d1d7cd96ca5f5&amp;linkname=Littorai%20Pinot%20Noir%20Sonoma%20County%20Sonoma%20Coast%20The%20Haven%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167588%2Flittorai-pinot-noir-sonoma-county-sonoma-coast-the-haven-vineyard-2019%2F%3Fsid%3De5cf98cbdba74cf5423d1d7cd96ca5f5&amp;linkname=Littorai%20Pinot%20Noir%20Sonoma%20County%20Sonoma%20Coast%20The%20Haven%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167588%2Flittorai-pinot-noir-sonoma-county-sonoma-coast-the-haven-vineyard-2019%2F%3Fsid%3De5cf98cbdba74cf5423d1d7cd96ca5f5&amp;linkname=Littorai%20Pinot%20Noir%20Sonoma%20County%20Sonoma%20Coast%20The%20Haven%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Littorai Pinot Noir Sonoma County Sonoma Coast The Haven Vineyard",url:"https://www.jamessuckling.com/tasting-notes/167588/littorai-pinot-noir-sonoma-county-sonoma-coast-the-haven-vineyard-2019/?sid=e5cf98cbdba74cf5423d1d7cd96ca5f5"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-38">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix" data-toggle="collapse" data-parent="#accordion-38" data-target="#collapse-38" aria-expanded="true">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">38</span><span class="title-vintage">Château Rauzan-Ségla Margaux 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse in" id="collapse-38" aria-expanded="true" style="">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Rauzan-Ségla Margaux/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of crushed blackberries and blueberries with dried flowers and bark, following through to a full body with a tight and powerful palate of beautiful fruit and chewy yet polished tannins that are compressed and impressive. Extremely linear and intense. Muscular, in a toned way. Yet it opens in the mouth at you taste it. 60% cabernet sauvignon and 40% merlot. Drink after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/144651/chateau-rauzan-segla-margaux-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_38"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144651%2Fchateau-rauzan-segla-margaux-2018%2F%3Fsid%3De9aaa248f88a7b346bcd01ed8f36b6b5&amp;linkname=Ch%C3%A2teau%20Rauzan-S%C3%A9gla%20Margaux" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144651%2Fchateau-rauzan-segla-margaux-2018%2F%3Fsid%3De9aaa248f88a7b346bcd01ed8f36b6b5&amp;linkname=Ch%C3%A2teau%20Rauzan-S%C3%A9gla%20Margaux" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144651%2Fchateau-rauzan-segla-margaux-2018%2F%3Fsid%3De9aaa248f88a7b346bcd01ed8f36b6b5&amp;linkname=Ch%C3%A2teau%20Rauzan-S%C3%A9gla%20Margaux" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144651%2Fchateau-rauzan-segla-margaux-2018%2F%3Fsid%3De9aaa248f88a7b346bcd01ed8f36b6b5&amp;linkname=Ch%C3%A2teau%20Rauzan-S%C3%A9gla%20Margaux" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Rauzan-S\u00e9gla Margaux",url:"https://www.jamessuckling.com/tasting-notes/144651/chateau-rauzan-segla-margaux-2018/?sid=e9aaa248f88a7b346bcd01ed8f36b6b5"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-39">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-39" data-target="#collapse-39">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">39</span><span class="title-vintage">Penfolds Shiraz South Australia St Henri 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-39">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">South Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Penfolds Shiraz South Australia St Henri/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A great St. Henri and, although multi-regional, this is very much a wine that speaks of the Barossa Valley, with aromas of ripe blackberries and red plums that are so fresh, together with tobacco, young-leather, earth, chocolate, coal-smoke and tarry accents. Effortless depth on the palate with summer berries, framed in fine, alabaster-like tannins that are underscored with discreet power. So long and captivating. A blend of Barossa Valley, McLaren Vale, Port Lincoln, Robe, Padthaway, Clare Valley and Adelaide Hills. Drink over the next decade or more. Screw cap.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/158481/penfolds-shiraz-south-australia-st-henri-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_39"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158481%2Fpenfolds-shiraz-south-australia-st-henri-2018%2F%3Fsid%3D4a6c08ffb9368d031f7457935470bd82&amp;linkname=Penfolds%20Shiraz%20South%20Australia%20St%20Henri" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158481%2Fpenfolds-shiraz-south-australia-st-henri-2018%2F%3Fsid%3D4a6c08ffb9368d031f7457935470bd82&amp;linkname=Penfolds%20Shiraz%20South%20Australia%20St%20Henri" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158481%2Fpenfolds-shiraz-south-australia-st-henri-2018%2F%3Fsid%3D4a6c08ffb9368d031f7457935470bd82&amp;linkname=Penfolds%20Shiraz%20South%20Australia%20St%20Henri" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158481%2Fpenfolds-shiraz-south-australia-st-henri-2018%2F%3Fsid%3D4a6c08ffb9368d031f7457935470bd82&amp;linkname=Penfolds%20Shiraz%20South%20Australia%20St%20Henri" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Penfolds Shiraz South Australia St Henri",url:"https://www.jamessuckling.com/tasting-notes/158481/penfolds-shiraz-south-australia-st-henri-2018/?sid=4a6c08ffb9368d031f7457935470bd82"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-40">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-40" data-target="#collapse-40">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">40</span><span class="title-vintage">Quintessa Napa Valley Rutherford 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-40">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Quintessa Napa Valley Rutherford/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is beautifully polished with firm, dusty tannins to the blue fruit, as well as chocolate and cedar character. Some much earthier character, too, from mushrooms to bark. Forest flowers. Perfumed. It’s full-bodied with round tannins and a soft, creamy finish. Some iron and iodine to this. So attractive at the finish. From biodynamically grown grapes. Better after 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/144652/quintessa-napa-valley-rutherford-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_40"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144652%2Fquintessa-napa-valley-rutherford-2018%2F%3Fsid%3Dcf619c469b1a657ffb4f164e9b713eda&amp;linkname=Quintessa%20Napa%20Valley%20Rutherford" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144652%2Fquintessa-napa-valley-rutherford-2018%2F%3Fsid%3Dcf619c469b1a657ffb4f164e9b713eda&amp;linkname=Quintessa%20Napa%20Valley%20Rutherford" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144652%2Fquintessa-napa-valley-rutherford-2018%2F%3Fsid%3Dcf619c469b1a657ffb4f164e9b713eda&amp;linkname=Quintessa%20Napa%20Valley%20Rutherford" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144652%2Fquintessa-napa-valley-rutherford-2018%2F%3Fsid%3Dcf619c469b1a657ffb4f164e9b713eda&amp;linkname=Quintessa%20Napa%20Valley%20Rutherford" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Quintessa Napa Valley Rutherford",url:"https://www.jamessuckling.com/tasting-notes/144652/quintessa-napa-valley-rutherford-2018/?sid=cf619c469b1a657ffb4f164e9b713eda"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-41">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-41" data-target="#collapse-41">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">41</span><span class="title-vintage">Susana Balbo Wines Malbec Agrelo Nosotros Single Vineyard Nómade 2017</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-41">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Argentina</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Mendoza</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2017</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Susana Balbo Wines Malbec Agrelo Nosotros Single Vineyard Nómade/2017/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Black plums, blueberries, dried herbs, cedar, vanilla and crushed stones on the nose. It’s medium-to full-bodied with ultra fine tannins and bright acidity. There’s vivacity and wild energy to this, with layers of bitter chocolate and berries interwoven with stones and minerals. So energetic and very driven with gorgeously integrated tannins. So long, too. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149473/susana-balbo-wines-malbec-agrelo-nosotros-single-vineyard-nomade-2017">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_41"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149473%2Fsusana-balbo-wines-malbec-agrelo-nosotros-single-vineyard-nomade-2017%2F%3Fsid%3Dbcf7e5c4d845934c46d981dd59d5d53e&amp;linkname=Susana%20Balbo%20Wines%20Malbec%20Agrelo%20Nosotros%20Single%20Vineyard%20N%C3%B3made" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149473%2Fsusana-balbo-wines-malbec-agrelo-nosotros-single-vineyard-nomade-2017%2F%3Fsid%3Dbcf7e5c4d845934c46d981dd59d5d53e&amp;linkname=Susana%20Balbo%20Wines%20Malbec%20Agrelo%20Nosotros%20Single%20Vineyard%20N%C3%B3made" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149473%2Fsusana-balbo-wines-malbec-agrelo-nosotros-single-vineyard-nomade-2017%2F%3Fsid%3Dbcf7e5c4d845934c46d981dd59d5d53e&amp;linkname=Susana%20Balbo%20Wines%20Malbec%20Agrelo%20Nosotros%20Single%20Vineyard%20N%C3%B3made" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149473%2Fsusana-balbo-wines-malbec-agrelo-nosotros-single-vineyard-nomade-2017%2F%3Fsid%3Dbcf7e5c4d845934c46d981dd59d5d53e&amp;linkname=Susana%20Balbo%20Wines%20Malbec%20Agrelo%20Nosotros%20Single%20Vineyard%20N%C3%B3made" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Susana Balbo Wines Malbec Agrelo Nosotros Single Vineyard N\u00f3made",url:"https://www.jamessuckling.com/tasting-notes/149473/susana-balbo-wines-malbec-agrelo-nosotros-single-vineyard-nomade-2017/?sid=bcf7e5c4d845934c46d981dd59d5d53e"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-42">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-42" data-target="#collapse-42">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">42</span><span class="title-vintage">Joseph Phelps Napa Valley Insignia 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-42">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Joseph Phelps Napa Valley Insignia/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Blackberry and black chocolate with mint, conifer and clove. Sweet tobacco, violets and flowers, too. Some graphite. Cool and complex. Full-bodied with ultra fine, dusty tannins and a wonderful, extremely long finish. Savory and refined. A classic-styled 2018. This needs time, but is so approachable and gorgeous. One of the best Insignias ever. Alive and changing all the time. 40% Stags Leap AVA.  87% cabernet sauvignon, 8% petit verdot, 3% malbec and 2% cabernet franc. Leave this for five or six years, but so wonderful now.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149470/joseph-phelps-napa-valley-insignia-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_42"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149470%2Fjoseph-phelps-napa-valley-insignia-2018%2F%3Fsid%3D9d43421376794c83531a36519084dba7&amp;linkname=Joseph%20Phelps%20Napa%20Valley%20Insignia" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149470%2Fjoseph-phelps-napa-valley-insignia-2018%2F%3Fsid%3D9d43421376794c83531a36519084dba7&amp;linkname=Joseph%20Phelps%20Napa%20Valley%20Insignia" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149470%2Fjoseph-phelps-napa-valley-insignia-2018%2F%3Fsid%3D9d43421376794c83531a36519084dba7&amp;linkname=Joseph%20Phelps%20Napa%20Valley%20Insignia" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149470%2Fjoseph-phelps-napa-valley-insignia-2018%2F%3Fsid%3D9d43421376794c83531a36519084dba7&amp;linkname=Joseph%20Phelps%20Napa%20Valley%20Insignia" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Joseph Phelps Napa Valley Insignia",url:"https://www.jamessuckling.com/tasting-notes/149470/joseph-phelps-napa-valley-insignia-2018/?sid=9d43421376794c83531a36519084dba7"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-43">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-43" data-target="#collapse-43">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">43</span><span class="title-vintage">Château La Fleur-Pétrus Pomerol 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-43">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château La Fleur-Pétrus Pomerol/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Ripe black fruit, clove, licorice, pine and walnut husk on the nose. Bitter chocolate and coffee, too. It’s full-bodied with firm, tight tannins. Muscular and very formed. Energetic and precise with long, chewy layers and lots of depth, structure and polish. Superb. Needs time. Try from 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145112/chateau-la-fleur-petrus-pomerol-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_43"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145112%2Fchateau-la-fleur-petrus-pomerol-2018%2F%3Fsid%3Dd692d456e4baf85cb9c6fad5c7394193&amp;linkname=Ch%C3%A2teau%20La%20Fleur-P%C3%A9trus%20Pomerol" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145112%2Fchateau-la-fleur-petrus-pomerol-2018%2F%3Fsid%3Dd692d456e4baf85cb9c6fad5c7394193&amp;linkname=Ch%C3%A2teau%20La%20Fleur-P%C3%A9trus%20Pomerol" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145112%2Fchateau-la-fleur-petrus-pomerol-2018%2F%3Fsid%3Dd692d456e4baf85cb9c6fad5c7394193&amp;linkname=Ch%C3%A2teau%20La%20Fleur-P%C3%A9trus%20Pomerol" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145112%2Fchateau-la-fleur-petrus-pomerol-2018%2F%3Fsid%3Dd692d456e4baf85cb9c6fad5c7394193&amp;linkname=Ch%C3%A2teau%20La%20Fleur-P%C3%A9trus%20Pomerol" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau La Fleur-P\u00e9trus Pomerol",url:"https://www.jamessuckling.com/tasting-notes/145112/chateau-la-fleur-petrus-pomerol-2018/?sid=d692d456e4baf85cb9c6fad5c7394193"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-44">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix" data-toggle="collapse" data-parent="#accordion-44" data-target="#collapse-44" aria-expanded="true">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">44</span><span class="title-vintage">Colgin Cellars Cabernet Sauvignon Napa Valley Tychson Hill 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse in" id="collapse-44" aria-expanded="true" style="">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Colgin Cellars Cabernet Sauvignon Napa Valley Tychson Hill/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Gorgeous dark-fruit aromas with blackcurrants, mushrooms, bark and flowers. Jasmine.  Full-bodied with wonderfully fine tannins. Finishes so long and agile. Sort of cloud-like. Blackberry and dark chocolate at the end. Totally integrated tannins. You feel them, but you don’t see them. Unique experience tasting this. A classic in the making. Cabernet sauvignon with a touch of petit verdot and cabernet franc. Try after 2027.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/147700/colgin-cellars-cabernet-sauvignon-napa-valley-tychson-hill-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_44"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147700%2Fcolgin-cellars-cabernet-sauvignon-napa-valley-tychson-hill-2018%2F%3Fsid%3D2f984282cd4ee2b1d88038e863b9c367&amp;linkname=Colgin%20Cellars%20Cabernet%20Sauvignon%20Napa%20Valley%20Tychson%20Hill" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147700%2Fcolgin-cellars-cabernet-sauvignon-napa-valley-tychson-hill-2018%2F%3Fsid%3D2f984282cd4ee2b1d88038e863b9c367&amp;linkname=Colgin%20Cellars%20Cabernet%20Sauvignon%20Napa%20Valley%20Tychson%20Hill" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147700%2Fcolgin-cellars-cabernet-sauvignon-napa-valley-tychson-hill-2018%2F%3Fsid%3D2f984282cd4ee2b1d88038e863b9c367&amp;linkname=Colgin%20Cellars%20Cabernet%20Sauvignon%20Napa%20Valley%20Tychson%20Hill" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147700%2Fcolgin-cellars-cabernet-sauvignon-napa-valley-tychson-hill-2018%2F%3Fsid%3D2f984282cd4ee2b1d88038e863b9c367&amp;linkname=Colgin%20Cellars%20Cabernet%20Sauvignon%20Napa%20Valley%20Tychson%20Hill" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Colgin Cellars Cabernet Sauvignon Napa Valley Tychson Hill",url:"https://www.jamessuckling.com/tasting-notes/147700/colgin-cellars-cabernet-sauvignon-napa-valley-tychson-hill-2018/?sid=2f984282cd4ee2b1d88038e863b9c367"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-45">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-45" data-target="#collapse-45">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">45</span><span class="title-vintage">Château Ducru-Beaucaillou St.-Julien 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-45">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Ducru-Beaucaillou St.-Julien/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of blackberries, blackcurrants, new leather and bark follow through to a full body with a dense, deep palate that goes on and on, but is still shy and reserved. Large amount of ultra fine, cashmere-like tannins that are silky, sleek and wonderfully integrated. Extremely long and focused. Needs at least four to five years to start opening. A beautiful wine for the cellar. Try after 2027.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145526/chateau-ducru-beaucaillou-st-julien-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_45"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145526%2Fchateau-ducru-beaucaillou-st-julien-2018%2F%3Fsid%3D55fb570d64d67cdd21fd74bb65ecb722&amp;linkname=Ch%C3%A2teau%20Ducru-Beaucaillou%20St.-Julien" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145526%2Fchateau-ducru-beaucaillou-st-julien-2018%2F%3Fsid%3D55fb570d64d67cdd21fd74bb65ecb722&amp;linkname=Ch%C3%A2teau%20Ducru-Beaucaillou%20St.-Julien" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145526%2Fchateau-ducru-beaucaillou-st-julien-2018%2F%3Fsid%3D55fb570d64d67cdd21fd74bb65ecb722&amp;linkname=Ch%C3%A2teau%20Ducru-Beaucaillou%20St.-Julien" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145526%2Fchateau-ducru-beaucaillou-st-julien-2018%2F%3Fsid%3D55fb570d64d67cdd21fd74bb65ecb722&amp;linkname=Ch%C3%A2teau%20Ducru-Beaucaillou%20St.-Julien" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Ducru-Beaucaillou St.-Julien",url:"https://www.jamessuckling.com/tasting-notes/145526/chateau-ducru-beaucaillou-st-julien-2018/?sid=55fb570d64d67cdd21fd74bb65ecb722"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-46">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-46" data-target="#collapse-46">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">46</span><span class="title-vintage">Dr. Bürklin-Wolf Riesling Pfalz Pechstein GC 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-46">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Pfalz</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Dr. Bürklin-Wolf Riesling Pfalz Pechstein GC/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">So stony, poised and pristine, in spite of all the concentration, this has staggering elegance and finesse for such a warm region. Mega minerality at the breathtakingly long and radical finish that defies any simple description. From biodynamically grown grapes. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/157938/dr-burklin-wolf-riesling-pfalz-pechstein-gc-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_46"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157938%2Fdr-burklin-wolf-riesling-pfalz-pechstein-gc-2020%2F%3Fsid%3Db2ee0e472eb420aa982bf0df788102ad&amp;linkname=Dr.%20B%C3%BCrklin-Wolf%20Riesling%20Pfalz%20Pechstein%20GC" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157938%2Fdr-burklin-wolf-riesling-pfalz-pechstein-gc-2020%2F%3Fsid%3Db2ee0e472eb420aa982bf0df788102ad&amp;linkname=Dr.%20B%C3%BCrklin-Wolf%20Riesling%20Pfalz%20Pechstein%20GC" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157938%2Fdr-burklin-wolf-riesling-pfalz-pechstein-gc-2020%2F%3Fsid%3Db2ee0e472eb420aa982bf0df788102ad&amp;linkname=Dr.%20B%C3%BCrklin-Wolf%20Riesling%20Pfalz%20Pechstein%20GC" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157938%2Fdr-burklin-wolf-riesling-pfalz-pechstein-gc-2020%2F%3Fsid%3Db2ee0e472eb420aa982bf0df788102ad&amp;linkname=Dr.%20B%C3%BCrklin-Wolf%20Riesling%20Pfalz%20Pechstein%20GC" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Dr. B\u00fcrklin-Wolf Riesling Pfalz Pechstein GC",url:"https://www.jamessuckling.com/tasting-notes/157938/dr-burklin-wolf-riesling-pfalz-pechstein-gc-2020/?sid=b2ee0e472eb420aa982bf0df788102ad"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-47">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-47" data-target="#collapse-47">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">47</span><span class="title-vintage">Catena Zapata Malbec Mendoza Argentino 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-47">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Argentina</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Mendoza</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Catena Zapata Malbec Mendoza Argentino/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is made from over 100-year-old vineyards and offers blackberries with blue fruit and dark chocolate. Shows bark and black truffle undertones, too. Tight and more focused than in past vintages. The quality of the tannins is more precise and fine. Blackberries and black truffles at the end. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149092/catena-zapata-malbec-mendoza-argentino-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_47"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149092%2Fcatena-zapata-malbec-mendoza-argentino-2019%2F%3Fsid%3Da1c39cc2db1e9753419faf22d3e12503&amp;linkname=Catena%20Zapata%20Malbec%20Mendoza%20Argentino" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149092%2Fcatena-zapata-malbec-mendoza-argentino-2019%2F%3Fsid%3Da1c39cc2db1e9753419faf22d3e12503&amp;linkname=Catena%20Zapata%20Malbec%20Mendoza%20Argentino" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149092%2Fcatena-zapata-malbec-mendoza-argentino-2019%2F%3Fsid%3Da1c39cc2db1e9753419faf22d3e12503&amp;linkname=Catena%20Zapata%20Malbec%20Mendoza%20Argentino" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149092%2Fcatena-zapata-malbec-mendoza-argentino-2019%2F%3Fsid%3Da1c39cc2db1e9753419faf22d3e12503&amp;linkname=Catena%20Zapata%20Malbec%20Mendoza%20Argentino" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Catena Zapata Malbec Mendoza Argentino",url:"https://www.jamessuckling.com/tasting-notes/149092/catena-zapata-malbec-mendoza-argentino-2019/?sid=a1c39cc2db1e9753419faf22d3e12503"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-48">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-48" data-target="#collapse-48">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">48</span><span class="title-vintage">Eredi Fuligni Brunello di Montalcino Riserva 2016</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-48">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2016</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Eredi Fuligni Brunello di Montalcino Riserva/2016/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">The complexity and beauty of this wine is something else on the nose, offering perfume, cedar, dried flower, black cherry, blueberry and crushed stone. Orange peel, too. Full-bodied with incredible layers of ultra-fine tannins that give this wine horizontal depth that almost seems endless. Extremely long and lightly chewy at the end. This is one for the cellar. Try after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/165082/eredi-fuligni-brunello-di-montalcino-riserva-2016">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_48"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165082%2Feredi-fuligni-brunello-di-montalcino-riserva-2016%2F%3Fsid%3Db6848277f559474451373b4243749e72&amp;linkname=Eredi%20Fuligni%20Brunello%20di%20Montalcino%20Riserva" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165082%2Feredi-fuligni-brunello-di-montalcino-riserva-2016%2F%3Fsid%3Db6848277f559474451373b4243749e72&amp;linkname=Eredi%20Fuligni%20Brunello%20di%20Montalcino%20Riserva" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165082%2Feredi-fuligni-brunello-di-montalcino-riserva-2016%2F%3Fsid%3Db6848277f559474451373b4243749e72&amp;linkname=Eredi%20Fuligni%20Brunello%20di%20Montalcino%20Riserva" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165082%2Feredi-fuligni-brunello-di-montalcino-riserva-2016%2F%3Fsid%3Db6848277f559474451373b4243749e72&amp;linkname=Eredi%20Fuligni%20Brunello%20di%20Montalcino%20Riserva" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Eredi Fuligni Brunello di Montalcino Riserva",url:"https://www.jamessuckling.com/tasting-notes/165082/eredi-fuligni-brunello-di-montalcino-riserva-2016/?sid=b6848277f559474451373b4243749e72"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-49">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-49" data-target="#collapse-49">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">49</span><span class="title-vintage">Antica Terra Pinot Noir Eola-Amity Hills Antikythera 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-49">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Oregon</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Antica Terra Pinot Noir Eola-Amity Hills Antikythera/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Wow. Aromas of blackberry, ripe strawberry, spice and smoke follow through to a full body with firm, minerally tannins that have a chalky, stony texture that gives it firmness and complexity. Very long and driven. Layered, too.  Spice, cinnamon stick, chocolate and dried berries. Try after 2025, but already joyous to taste or drink. Only about 400 cases made.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/148639/antica-terra-pinot-noir-eola-amity-hills-antikythera-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_49"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148639%2Fantica-terra-pinot-noir-eola-amity-hills-antikythera-2018%2F%3Fsid%3D84de5cf96fb7fe6b95f1bc811f746921&amp;linkname=Antica%20Terra%20Pinot%20Noir%20Eola-Amity%20Hills%20Antikythera" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148639%2Fantica-terra-pinot-noir-eola-amity-hills-antikythera-2018%2F%3Fsid%3D84de5cf96fb7fe6b95f1bc811f746921&amp;linkname=Antica%20Terra%20Pinot%20Noir%20Eola-Amity%20Hills%20Antikythera" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148639%2Fantica-terra-pinot-noir-eola-amity-hills-antikythera-2018%2F%3Fsid%3D84de5cf96fb7fe6b95f1bc811f746921&amp;linkname=Antica%20Terra%20Pinot%20Noir%20Eola-Amity%20Hills%20Antikythera" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148639%2Fantica-terra-pinot-noir-eola-amity-hills-antikythera-2018%2F%3Fsid%3D84de5cf96fb7fe6b95f1bc811f746921&amp;linkname=Antica%20Terra%20Pinot%20Noir%20Eola-Amity%20Hills%20Antikythera" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Antica Terra Pinot Noir Eola-Amity Hills Antikythera",url:"https://www.jamessuckling.com/tasting-notes/148639/antica-terra-pinot-noir-eola-amity-hills-antikythera-2018/?sid=84de5cf96fb7fe6b95f1bc811f746921"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-50">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-50" data-target="#collapse-50">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">50</span><span class="title-vintage">Dana Estates Napa Valley Lotus Vineyard 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-50">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Dana Estates Napa Valley Lotus Vineyard/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Seductive aromas of blackberries, blackcurrants, black olives, pine needles and violets follow through to a full body. The tannins are so poised and dynamic, while being extremely fine and focused. It goes on for minutes. Caresses every millimeter of your palate. A truly great 2018 that highlights the balance, finesse and refinement of the vintage. Needs time to come completely together. Try after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/150375/dana-estates-napa-valley-lotus-vineyard-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_50"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F150375%2Fdana-estates-napa-valley-lotus-vineyard-2018%2F%3Fsid%3D3cc816e07f8435384de467d964159085&amp;linkname=Dana%20Estates%20Napa%20Valley%20Lotus%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F150375%2Fdana-estates-napa-valley-lotus-vineyard-2018%2F%3Fsid%3D3cc816e07f8435384de467d964159085&amp;linkname=Dana%20Estates%20Napa%20Valley%20Lotus%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F150375%2Fdana-estates-napa-valley-lotus-vineyard-2018%2F%3Fsid%3D3cc816e07f8435384de467d964159085&amp;linkname=Dana%20Estates%20Napa%20Valley%20Lotus%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F150375%2Fdana-estates-napa-valley-lotus-vineyard-2018%2F%3Fsid%3D3cc816e07f8435384de467d964159085&amp;linkname=Dana%20Estates%20Napa%20Valley%20Lotus%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Dana Estates Napa Valley Lotus Vineyard",url:"https://www.jamessuckling.com/tasting-notes/150375/dana-estates-napa-valley-lotus-vineyard-2018/?sid=3cc816e07f8435384de467d964159085"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-51">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-51" data-target="#collapse-51">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">51</span><span class="title-vintage">Château Margaux Margaux 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-51">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Margaux Margaux/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">So much ash, tobacco and earth to the bright blackberry and currant aromas. Flowers too. Fresh. Full-bodied with seamless tannins that spread across your palate and caress every square centimeter. It’s shows loads of ripe-berry, cherry, currant and chocolate character, as well as walnut and light cedar. Then the finish goes on for minutes. Extremely refined and elegant, despite the structure. 90% cabernet sauvignon, 4% cabernet franc, 4% merlot and 2% petit verdot. A joy to taste, but drink after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145109/chateau-margaux-margaux-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_51"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145109%2Fchateau-margaux-margaux-2018%2F%3Fsid%3D42f71aaab73ea8e4a4b3a19394cc9222&amp;linkname=Ch%C3%A2teau%20Margaux%20Margaux" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145109%2Fchateau-margaux-margaux-2018%2F%3Fsid%3D42f71aaab73ea8e4a4b3a19394cc9222&amp;linkname=Ch%C3%A2teau%20Margaux%20Margaux" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145109%2Fchateau-margaux-margaux-2018%2F%3Fsid%3D42f71aaab73ea8e4a4b3a19394cc9222&amp;linkname=Ch%C3%A2teau%20Margaux%20Margaux" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145109%2Fchateau-margaux-margaux-2018%2F%3Fsid%3D42f71aaab73ea8e4a4b3a19394cc9222&amp;linkname=Ch%C3%A2teau%20Margaux%20Margaux" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Margaux Margaux",url:"https://www.jamessuckling.com/tasting-notes/145109/chateau-margaux-margaux-2018/?sid=42f71aaab73ea8e4a4b3a19394cc9222"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-52">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-52" data-target="#collapse-52">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">52</span><span class="title-vintage">Zuccardi Malbec Valle de Uco Paraje Altamira Finca Piedra Infinita 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-52">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Argentina</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Mendoza</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Zuccardi Malbec Valle de Uco Paraje Altamira Finca Piedra Infinita/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of crushed fruit with mushrooms, dried flowers, ash, charcoal, iodine and bark, following through to a full-bodied palate with superb depth of fruit and layers of polished, fine tannins. Extremely long and seamless. A beauty by all accounts. Complex. Juicy. Supple. Better after 2023, when it will give you all it has stored up in goodness, character and uniqueness.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149475/zuccardi-malbec-valle-de-uco-paraje-altamira-finca-piedra-infinita-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_52"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149475%2Fzuccardi-malbec-valle-de-uco-paraje-altamira-finca-piedra-infinita-2018%2F%3Fsid%3D2d984fea43506ffb6dc3191c9436da06&amp;linkname=Zuccardi%20Malbec%20Valle%20de%20Uco%20Paraje%20Altamira%20Finca%20Piedra%20Infinita" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149475%2Fzuccardi-malbec-valle-de-uco-paraje-altamira-finca-piedra-infinita-2018%2F%3Fsid%3D2d984fea43506ffb6dc3191c9436da06&amp;linkname=Zuccardi%20Malbec%20Valle%20de%20Uco%20Paraje%20Altamira%20Finca%20Piedra%20Infinita" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149475%2Fzuccardi-malbec-valle-de-uco-paraje-altamira-finca-piedra-infinita-2018%2F%3Fsid%3D2d984fea43506ffb6dc3191c9436da06&amp;linkname=Zuccardi%20Malbec%20Valle%20de%20Uco%20Paraje%20Altamira%20Finca%20Piedra%20Infinita" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149475%2Fzuccardi-malbec-valle-de-uco-paraje-altamira-finca-piedra-infinita-2018%2F%3Fsid%3D2d984fea43506ffb6dc3191c9436da06&amp;linkname=Zuccardi%20Malbec%20Valle%20de%20Uco%20Paraje%20Altamira%20Finca%20Piedra%20Infinita" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Zuccardi Malbec Valle de Uco Paraje Altamira Finca Piedra Infinita",url:"https://www.jamessuckling.com/tasting-notes/149475/zuccardi-malbec-valle-de-uco-paraje-altamira-finca-piedra-infinita-2018/?sid=2d984fea43506ffb6dc3191c9436da06"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-53">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-53" data-target="#collapse-53">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">53</span><span class="title-vintage">L’If St.-Emilion  2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-53">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/L’If St.-Emilion /2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of black cherries, blueberries, licorice, dried lavender, nutmeg and grated milk chocolate. Pure raspberries, walnut husks and crushed peppercorns as well. It’s full-bodied with firm, racy tannins that go on for minutes. So sleek and polished with a long finish. Really amazing and perhaps the best wine ever from here. Same ownership as the legendary Le Pin from Pomerol. Slightly more cabernet franc (30% instead of 20%)  in the blend may have made the difference. The rest is merlot. Clearly the best wine ever from here, since the official first vintage 2011. Try from 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145531/lif-st-emilion-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_53"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145531%2Flif-st-emilion-2018%2F%3Fsid%3D0941d80b096b8853ec5c648938f3b250&amp;linkname=L%E2%80%99If%20St.-Emilion%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145531%2Flif-st-emilion-2018%2F%3Fsid%3D0941d80b096b8853ec5c648938f3b250&amp;linkname=L%E2%80%99If%20St.-Emilion%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145531%2Flif-st-emilion-2018%2F%3Fsid%3D0941d80b096b8853ec5c648938f3b250&amp;linkname=L%E2%80%99If%20St.-Emilion%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145531%2Flif-st-emilion-2018%2F%3Fsid%3D0941d80b096b8853ec5c648938f3b250&amp;linkname=L%E2%80%99If%20St.-Emilion%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"L\u2019If St.-Emilion ",url:"https://www.jamessuckling.com/tasting-notes/145531/lif-st-emilion-2018/?sid=0941d80b096b8853ec5c648938f3b250"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-54">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-54" data-target="#collapse-54">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">54</span><span class="title-vintage">Château Beauséjour Duffau-Lagarrosse St.-Emilion 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-54">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Beauséjour Duffau-Lagarrosse St.-Emilion/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of blackcurrant, ripe blackberry, black olive, oyster shell and black tea. Some ash and dried flowers, too. It’s medium-to full-bodied with firm, tight-grained tannins. Sleek and compact with a savory, mineral finish. Great length and depth. Wonderful texture. Such precision. Try from 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145524/chateau-beausejour-duffau-lagarrosse-st-emilion-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_54"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145524%2Fchateau-beausejour-duffau-lagarrosse-st-emilion-2018%2F%3Fsid%3D8939f7625510822671a35924871995ae&amp;linkname=Ch%C3%A2teau%20Beaus%C3%A9jour%20Duffau-Lagarrosse%20St.-Emilion" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145524%2Fchateau-beausejour-duffau-lagarrosse-st-emilion-2018%2F%3Fsid%3D8939f7625510822671a35924871995ae&amp;linkname=Ch%C3%A2teau%20Beaus%C3%A9jour%20Duffau-Lagarrosse%20St.-Emilion" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145524%2Fchateau-beausejour-duffau-lagarrosse-st-emilion-2018%2F%3Fsid%3D8939f7625510822671a35924871995ae&amp;linkname=Ch%C3%A2teau%20Beaus%C3%A9jour%20Duffau-Lagarrosse%20St.-Emilion" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145524%2Fchateau-beausejour-duffau-lagarrosse-st-emilion-2018%2F%3Fsid%3D8939f7625510822671a35924871995ae&amp;linkname=Ch%C3%A2teau%20Beaus%C3%A9jour%20Duffau-Lagarrosse%20St.-Emilion" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Beaus\u00e9jour Duffau-Lagarrosse St.-Emilion",url:"https://www.jamessuckling.com/tasting-notes/145524/chateau-beausejour-duffau-lagarrosse-st-emilion-2018/?sid=8939f7625510822671a35924871995ae"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-55">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-55" data-target="#collapse-55">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">55</span><span class="title-vintage">Opus One Napa Valley 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-55">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Opus One Napa Valley/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Extremely perfumed and floral with lavender, lilacs and violets to the sweet, ripe berries,  such as blackberries and blackcurrants. Some slate and graphite, too. It’s full-bodied, yet ever so balanced and refined, with super fine tannins that last for minutes. Fresh herbs, such as bay leaf and lemon grass highlight the dark fruit. The quality of tannin is exquisite with wonderful polish and refinement. Lasts for minutes. So wonderful to taste now, but better after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/159052/opus-one-napa-valley-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_55"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159052%2Fopus-one-napa-valley-2018%2F%3Fsid%3D9e8aca89fd09db758abbd6761b89e5d7&amp;linkname=Opus%20One%20Napa%20Valley" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159052%2Fopus-one-napa-valley-2018%2F%3Fsid%3D9e8aca89fd09db758abbd6761b89e5d7&amp;linkname=Opus%20One%20Napa%20Valley" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159052%2Fopus-one-napa-valley-2018%2F%3Fsid%3D9e8aca89fd09db758abbd6761b89e5d7&amp;linkname=Opus%20One%20Napa%20Valley" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159052%2Fopus-one-napa-valley-2018%2F%3Fsid%3D9e8aca89fd09db758abbd6761b89e5d7&amp;linkname=Opus%20One%20Napa%20Valley" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Opus One Napa Valley",url:"https://www.jamessuckling.com/tasting-notes/159052/opus-one-napa-valley-2018/?sid=9e8aca89fd09db758abbd6761b89e5d7"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-56">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-56" data-target="#collapse-56">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">56</span><span class="title-vintage">Bernhard Huber Spätburgunder Baden Wildenstein GG 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-56">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Baden</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Bernhard Huber Spätburgunder Baden Wildenstein GG/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Pinot fans who haven’t yet registered the recent developments in Germany are strongly advised to taste this masterpiece, The cornucopia of red berries, cherries and flowers on the nose of this extraordinary wine bowls you over. Gigantic concentration, yet it remains so bright and elegant, thanks to the stunning intensity of extremely fine tannins.  Seamless finish that stretches out towards infinity. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/163966/bernhard-huber-spatburgunder-baden-wildenstein-gg-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_56"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163966%2Fbernhard-huber-spatburgunder-baden-wildenstein-gg-2019%2F%3Fsid%3D23378a8f31c233f65acb5213e36ed99f&amp;linkname=Bernhard%20Huber%20Sp%C3%A4tburgunder%20Baden%20Wildenstein%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163966%2Fbernhard-huber-spatburgunder-baden-wildenstein-gg-2019%2F%3Fsid%3D23378a8f31c233f65acb5213e36ed99f&amp;linkname=Bernhard%20Huber%20Sp%C3%A4tburgunder%20Baden%20Wildenstein%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163966%2Fbernhard-huber-spatburgunder-baden-wildenstein-gg-2019%2F%3Fsid%3D23378a8f31c233f65acb5213e36ed99f&amp;linkname=Bernhard%20Huber%20Sp%C3%A4tburgunder%20Baden%20Wildenstein%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163966%2Fbernhard-huber-spatburgunder-baden-wildenstein-gg-2019%2F%3Fsid%3D23378a8f31c233f65acb5213e36ed99f&amp;linkname=Bernhard%20Huber%20Sp%C3%A4tburgunder%20Baden%20Wildenstein%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Bernhard Huber Sp\u00e4tburgunder Baden Wildenstein GG",url:"https://www.jamessuckling.com/tasting-notes/163966/bernhard-huber-spatburgunder-baden-wildenstein-gg-2019/?sid=23378a8f31c233f65acb5213e36ed99f"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-57">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-57" data-target="#collapse-57">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">57</span><span class="title-vintage">Bond Napa Valley Vecina 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-57">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Bond Napa Valley Vecina/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Seductive aromas of blackcurrants, plums and flowers, including roses. Really incredible this year with such verticality, depth and brightness. Goes on and on and on. Superb fruit character with plums and currants. Love it. Drinkable now, but give it time. Try after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/152749/bond-napa-valley-vecina-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_57"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152749%2Fbond-napa-valley-vecina-2018%2F%3Fsid%3Dc701528338502fec9143a969864af5c3&amp;linkname=Bond%20Napa%20Valley%20Vecina" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152749%2Fbond-napa-valley-vecina-2018%2F%3Fsid%3Dc701528338502fec9143a969864af5c3&amp;linkname=Bond%20Napa%20Valley%20Vecina" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152749%2Fbond-napa-valley-vecina-2018%2F%3Fsid%3Dc701528338502fec9143a969864af5c3&amp;linkname=Bond%20Napa%20Valley%20Vecina" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152749%2Fbond-napa-valley-vecina-2018%2F%3Fsid%3Dc701528338502fec9143a969864af5c3&amp;linkname=Bond%20Napa%20Valley%20Vecina" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Bond Napa Valley Vecina",url:"https://www.jamessuckling.com/tasting-notes/152749/bond-napa-valley-vecina-2018/?sid=c701528338502fec9143a969864af5c3"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-58">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-58" data-target="#collapse-58">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">58</span><span class="title-vintage">Harlan Estate Napa Valley 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-58">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Harlan Estate Napa Valley/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Classy earth, oak and bay-leaf character on the nose, together with dark fruit, such as currants and blackberries. Forest flowers, too. Full-to medium-bodied, linear and tight with coolness and freshness. Mint and spearmint to the dark fruit. Lasts a long time. Such balance and intensity. Tight now, but great energy and length this year. Incredibly sophisticated and seductive. A joy to taste now, but try in 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/152750/harlan-estate-napa-valley-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_58"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152750%2Fharlan-estate-napa-valley-2018%2F%3Fsid%3D3dc8b5bdcb1f0abc85b166448d1ec462&amp;linkname=Harlan%20Estate%20Napa%20Valley" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152750%2Fharlan-estate-napa-valley-2018%2F%3Fsid%3D3dc8b5bdcb1f0abc85b166448d1ec462&amp;linkname=Harlan%20Estate%20Napa%20Valley" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152750%2Fharlan-estate-napa-valley-2018%2F%3Fsid%3D3dc8b5bdcb1f0abc85b166448d1ec462&amp;linkname=Harlan%20Estate%20Napa%20Valley" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152750%2Fharlan-estate-napa-valley-2018%2F%3Fsid%3D3dc8b5bdcb1f0abc85b166448d1ec462&amp;linkname=Harlan%20Estate%20Napa%20Valley" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Harlan Estate Napa Valley",url:"https://www.jamessuckling.com/tasting-notes/152750/harlan-estate-napa-valley-2018/?sid=3dc8b5bdcb1f0abc85b166448d1ec462"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-59">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-59" data-target="#collapse-59">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">59</span><span class="title-vintage">Château Lafleur Pomerol 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-59">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Lafleur Pomerol/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">So subtle and complex with blackberry, blueberry, fresh bark, fresh black truffles and light wet earth, as well as forest floor. Full-bodied, yet linear and so long with an amazingly polished and refined tannin structure and finesse that draws you deep and down in the palate. It opens incredibly in the glass. What a wine. Goes on for minutes. A real beauty. Something so true and ethereal here. Try after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145971/chateau-lafleur-pomerol-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_59"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145971%2Fchateau-lafleur-pomerol-2018%2F%3Fsid%3D1377245015d22fe78c06ead1e301b74c&amp;linkname=Ch%C3%A2teau%20Lafleur%20Pomerol" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145971%2Fchateau-lafleur-pomerol-2018%2F%3Fsid%3D1377245015d22fe78c06ead1e301b74c&amp;linkname=Ch%C3%A2teau%20Lafleur%20Pomerol" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145971%2Fchateau-lafleur-pomerol-2018%2F%3Fsid%3D1377245015d22fe78c06ead1e301b74c&amp;linkname=Ch%C3%A2teau%20Lafleur%20Pomerol" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145971%2Fchateau-lafleur-pomerol-2018%2F%3Fsid%3D1377245015d22fe78c06ead1e301b74c&amp;linkname=Ch%C3%A2teau%20Lafleur%20Pomerol" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Lafleur Pomerol",url:"https://www.jamessuckling.com/tasting-notes/145971/chateau-lafleur-pomerol-2018/?sid=1377245015d22fe78c06ead1e301b74c"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-60">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-60" data-target="#collapse-60">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">60</span><span class="title-vintage">Christmann Riesling Pfalz Idig GG 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-60">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Pfalz</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Christmann Riesling Pfalz Idig GG/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">So deep, it feels like it’s pulling you in the direction of the center of the earth! Yet, another side of the wine seems to float above the world. Radically mineral finish that leaves you in no doubt about this great dry riesling’s future! From biodynamically grown grapes with Respekt certification. Drinkable now, but best from 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/157942/christmann-riesling-pfalz-idig-gg-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_60"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157942%2Fchristmann-riesling-pfalz-idig-gg-2020%2F%3Fsid%3Dac668f1fecba1c4c5a6eef5fbdacc276&amp;linkname=Christmann%20Riesling%20Pfalz%20Idig%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157942%2Fchristmann-riesling-pfalz-idig-gg-2020%2F%3Fsid%3Dac668f1fecba1c4c5a6eef5fbdacc276&amp;linkname=Christmann%20Riesling%20Pfalz%20Idig%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157942%2Fchristmann-riesling-pfalz-idig-gg-2020%2F%3Fsid%3Dac668f1fecba1c4c5a6eef5fbdacc276&amp;linkname=Christmann%20Riesling%20Pfalz%20Idig%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F157942%2Fchristmann-riesling-pfalz-idig-gg-2020%2F%3Fsid%3Dac668f1fecba1c4c5a6eef5fbdacc276&amp;linkname=Christmann%20Riesling%20Pfalz%20Idig%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Christmann Riesling Pfalz Idig GG",url:"https://www.jamessuckling.com/tasting-notes/157942/christmann-riesling-pfalz-idig-gg-2020/?sid=ac668f1fecba1c4c5a6eef5fbdacc276"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-61">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix" data-toggle="collapse" data-parent="#accordion-61" data-target="#collapse-61" aria-expanded="true">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">61</span><span class="title-vintage">Bibi Graetz Toscana Colore 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse in" id="collapse-61" aria-expanded="true" style="">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Bibi Graetz Toscana Colore/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is so perfumed and seductive, with blackberries, cherries, dried flowers and perfume. It’s full-bodied and tight with very fine tannins. Really structured and long. Superb tannin texture. So fine, yet so powerful. This is an incredible combination of fruit and structure. Old-vine magic. Drink after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/158506/bibi-graetz-toscana-colore-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_61"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158506%2Fbibi-graetz-toscana-colore-2019%2F%3Fsid%3D631dd44f2b9a8ffaad4f4e4ab7322578&amp;linkname=Bibi%20Graetz%20Toscana%20Colore" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158506%2Fbibi-graetz-toscana-colore-2019%2F%3Fsid%3D631dd44f2b9a8ffaad4f4e4ab7322578&amp;linkname=Bibi%20Graetz%20Toscana%20Colore" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158506%2Fbibi-graetz-toscana-colore-2019%2F%3Fsid%3D631dd44f2b9a8ffaad4f4e4ab7322578&amp;linkname=Bibi%20Graetz%20Toscana%20Colore" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F158506%2Fbibi-graetz-toscana-colore-2019%2F%3Fsid%3D631dd44f2b9a8ffaad4f4e4ab7322578&amp;linkname=Bibi%20Graetz%20Toscana%20Colore" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Bibi Graetz Toscana Colore",url:"https://www.jamessuckling.com/tasting-notes/158506/bibi-graetz-toscana-colore-2019/?sid=631dd44f2b9a8ffaad4f4e4ab7322578"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-62">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-62" data-target="#collapse-62">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">62</span><span class="title-vintage">K Vintners Syrah Yakima Valley Motor City Kitty 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-62">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Washington</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/K Vintners Syrah Yakima Valley Motor City Kitty/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">There’s real purity of fruit to this with blackberry, blueberry and dark chocolate, as well as crushed-stone undertones. It’s full and focused with structure and purity. Transparent energy to this. Needs a couple of years. Better in 2023 onwards.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/152759/k-vintners-syrah-yakima-valley-motor-city-kitty-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_62"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152759%2Fk-vintners-syrah-yakima-valley-motor-city-kitty-2018%2F%3Fsid%3D6e570caee409ee6887113e432d1475a0&amp;linkname=K%20Vintners%20Syrah%20Yakima%20Valley%20Motor%20City%20Kitty" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152759%2Fk-vintners-syrah-yakima-valley-motor-city-kitty-2018%2F%3Fsid%3D6e570caee409ee6887113e432d1475a0&amp;linkname=K%20Vintners%20Syrah%20Yakima%20Valley%20Motor%20City%20Kitty" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152759%2Fk-vintners-syrah-yakima-valley-motor-city-kitty-2018%2F%3Fsid%3D6e570caee409ee6887113e432d1475a0&amp;linkname=K%20Vintners%20Syrah%20Yakima%20Valley%20Motor%20City%20Kitty" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F152759%2Fk-vintners-syrah-yakima-valley-motor-city-kitty-2018%2F%3Fsid%3D6e570caee409ee6887113e432d1475a0&amp;linkname=K%20Vintners%20Syrah%20Yakima%20Valley%20Motor%20City%20Kitty" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"K Vintners Syrah Yakima Valley Motor City Kitty",url:"https://www.jamessuckling.com/tasting-notes/152759/k-vintners-syrah-yakima-valley-motor-city-kitty-2018/?sid=6e570caee409ee6887113e432d1475a0"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-63">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-63" data-target="#collapse-63">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">63</span><span class="title-vintage">Bryant Family Vineyard Cabernet Sauvignon Napa Valley  2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-63">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Bryant Family Vineyard Cabernet Sauvignon Napa Valley /2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">100</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of blackberries and gun powder with some graphite and black licorice. Tile, too, with some conifer and cedar. Complex and enticing. Full-bodied with polished tannins that build on the palate and coat and caress every millimeter of your mouth. Encompassing and balanced mouth feel. A classic beauty.  Really tells where it is from! Great estate red. 600 cases. Try after 2027, but already a joy to taste.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/147297/bryant-family-vineyard-cabernet-sauvignon-napa-valley-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_63"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147297%2Fbryant-family-vineyard-cabernet-sauvignon-napa-valley-2018%2F%3Fsid%3Df91a0c1ce89df991a2dcf69777fd9857&amp;linkname=Bryant%20Family%20Vineyard%20Cabernet%20Sauvignon%20Napa%20Valley%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147297%2Fbryant-family-vineyard-cabernet-sauvignon-napa-valley-2018%2F%3Fsid%3Df91a0c1ce89df991a2dcf69777fd9857&amp;linkname=Bryant%20Family%20Vineyard%20Cabernet%20Sauvignon%20Napa%20Valley%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147297%2Fbryant-family-vineyard-cabernet-sauvignon-napa-valley-2018%2F%3Fsid%3Df91a0c1ce89df991a2dcf69777fd9857&amp;linkname=Bryant%20Family%20Vineyard%20Cabernet%20Sauvignon%20Napa%20Valley%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F147297%2Fbryant-family-vineyard-cabernet-sauvignon-napa-valley-2018%2F%3Fsid%3Df91a0c1ce89df991a2dcf69777fd9857&amp;linkname=Bryant%20Family%20Vineyard%20Cabernet%20Sauvignon%20Napa%20Valley%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Bryant Family Vineyard Cabernet Sauvignon Napa Valley ",url:"https://www.jamessuckling.com/tasting-notes/147297/bryant-family-vineyard-cabernet-sauvignon-napa-valley-2018/?sid=f91a0c1ce89df991a2dcf69777fd9857"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-64">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-64" data-target="#collapse-64">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">64</span><span class="title-vintage">Château Léoville Las Cases St.-Julien 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-64">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Léoville Las Cases St.-Julien/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">An elegant, complex nose of blackberries, blueberries and herbal and spice notes with dark-chocolate and earthy undertones. Violets, flowers and graphite, too. It’s full-bodied with firm, layered tannins and a crushed-stone undertone throughout the fresh, velvety and layered palate. Very complex, muscular and formed. The finish is endless. Lowest percentage of press wine ever in this. So deep. Try after 2027.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145113/chateau-leoville-las-cases-st-julien-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_64"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145113%2Fchateau-leoville-las-cases-st-julien-2018%2F%3Fsid%3D11472fddb3406fbca8e012f69dc91322&amp;linkname=Ch%C3%A2teau%20L%C3%A9oville%20Las%20Cases%20St.-Julien" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145113%2Fchateau-leoville-las-cases-st-julien-2018%2F%3Fsid%3D11472fddb3406fbca8e012f69dc91322&amp;linkname=Ch%C3%A2teau%20L%C3%A9oville%20Las%20Cases%20St.-Julien" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145113%2Fchateau-leoville-las-cases-st-julien-2018%2F%3Fsid%3D11472fddb3406fbca8e012f69dc91322&amp;linkname=Ch%C3%A2teau%20L%C3%A9oville%20Las%20Cases%20St.-Julien" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145113%2Fchateau-leoville-las-cases-st-julien-2018%2F%3Fsid%3D11472fddb3406fbca8e012f69dc91322&amp;linkname=Ch%C3%A2teau%20L%C3%A9oville%20Las%20Cases%20St.-Julien" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau L\u00e9oville Las Cases St.-Julien",url:"https://www.jamessuckling.com/tasting-notes/145113/chateau-leoville-las-cases-st-julien-2018/?sid=11472fddb3406fbca8e012f69dc91322"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-65">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-65" data-target="#collapse-65">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">65</span><span class="title-vintage">Petrolo Valdarno di Sopra Galatrona 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-65">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Petrolo Valdarno di Sopra Galatrona/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Blackberries and black cherries with lavender and violets on the nose. Full-bodied with velvety, chewy tannins, yet the fruit is very intense with vibrancy and energy. Muscular, yet agile. Pure and poised. A unique definition of merlot in Tuscany. Drink after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/159878/petrolo-valdarno-di-sopra-galatrona-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_65"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159878%2Fpetrolo-valdarno-di-sopra-galatrona-2019%2F%3Fsid%3D2bc615ff90868e296e39cba9eed6154a&amp;linkname=Petrolo%20Valdarno%20di%20Sopra%20Galatrona" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159878%2Fpetrolo-valdarno-di-sopra-galatrona-2019%2F%3Fsid%3D2bc615ff90868e296e39cba9eed6154a&amp;linkname=Petrolo%20Valdarno%20di%20Sopra%20Galatrona" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159878%2Fpetrolo-valdarno-di-sopra-galatrona-2019%2F%3Fsid%3D2bc615ff90868e296e39cba9eed6154a&amp;linkname=Petrolo%20Valdarno%20di%20Sopra%20Galatrona" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159878%2Fpetrolo-valdarno-di-sopra-galatrona-2019%2F%3Fsid%3D2bc615ff90868e296e39cba9eed6154a&amp;linkname=Petrolo%20Valdarno%20di%20Sopra%20Galatrona" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Petrolo Valdarno di Sopra Galatrona",url:"https://www.jamessuckling.com/tasting-notes/159878/petrolo-valdarno-di-sopra-galatrona-2019/?sid=2bc615ff90868e296e39cba9eed6154a"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-66">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-66" data-target="#collapse-66">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">66</span><span class="title-vintage">Château L'Église Clinet Pomerol 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-66">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château L'Église Clinet Pomerol/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Incredible purity of fruit here with blackberry, black olive, concrete, stone and violet in the nose. It’s full-bodied with a powerful palate of fruit that shows a wet-earth and black-truffle undertone. The tannins are intense and chewy, yet wonderfully polished and poised. Superb length in the finish. One built for long cellaring. Try after 2027.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145527/chateau-leglise-clinet-pomerol-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_66"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145527%2Fchateau-leglise-clinet-pomerol-2018%2F%3Fsid%3D7d3e60ecb1d23f42da6f96d74694a7a0&amp;linkname=Ch%C3%A2teau%20L%27%C3%89glise%20Clinet%20Pomerol" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145527%2Fchateau-leglise-clinet-pomerol-2018%2F%3Fsid%3D7d3e60ecb1d23f42da6f96d74694a7a0&amp;linkname=Ch%C3%A2teau%20L%27%C3%89glise%20Clinet%20Pomerol" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145527%2Fchateau-leglise-clinet-pomerol-2018%2F%3Fsid%3D7d3e60ecb1d23f42da6f96d74694a7a0&amp;linkname=Ch%C3%A2teau%20L%27%C3%89glise%20Clinet%20Pomerol" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145527%2Fchateau-leglise-clinet-pomerol-2018%2F%3Fsid%3D7d3e60ecb1d23f42da6f96d74694a7a0&amp;linkname=Ch%C3%A2teau%20L%27%C3%89glise%20Clinet%20Pomerol" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau L'\u00c9glise Clinet Pomerol",url:"https://www.jamessuckling.com/tasting-notes/145527/chateau-leglise-clinet-pomerol-2018/?sid=7d3e60ecb1d23f42da6f96d74694a7a0"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-67">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-67" data-target="#collapse-67">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">67</span><span class="title-vintage">Viña Cobos Malbec Los Arboles Valle de Uco Chañares Estate 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-67">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Argentina</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Mendoza</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Viña Cobos Malbec Los Arboles Valle de Uco Chañares Estate/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Blackberries, ink and blueberries with black-tea and bark undertones. Full-bodied with density and richness that is well framed with beautiful, round and polished tannins and a seamless texture. Goes on for minutes. Try after 2026, but already great.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149204/vina-cobos-malbec-los-arboles-valle-de-uco-chanares-estate-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_67"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149204%2Fvina-cobos-malbec-los-arboles-valle-de-uco-chanares-estate-2018%2F%3Fsid%3D8f77ccb003870776e6ebe7d2a97c59cb&amp;linkname=Vi%C3%B1a%20Cobos%20Malbec%20Los%20Arboles%20Valle%20de%20Uco%20Cha%C3%B1ares%20Estate" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149204%2Fvina-cobos-malbec-los-arboles-valle-de-uco-chanares-estate-2018%2F%3Fsid%3D8f77ccb003870776e6ebe7d2a97c59cb&amp;linkname=Vi%C3%B1a%20Cobos%20Malbec%20Los%20Arboles%20Valle%20de%20Uco%20Cha%C3%B1ares%20Estate" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149204%2Fvina-cobos-malbec-los-arboles-valle-de-uco-chanares-estate-2018%2F%3Fsid%3D8f77ccb003870776e6ebe7d2a97c59cb&amp;linkname=Vi%C3%B1a%20Cobos%20Malbec%20Los%20Arboles%20Valle%20de%20Uco%20Cha%C3%B1ares%20Estate" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149204%2Fvina-cobos-malbec-los-arboles-valle-de-uco-chanares-estate-2018%2F%3Fsid%3D8f77ccb003870776e6ebe7d2a97c59cb&amp;linkname=Vi%C3%B1a%20Cobos%20Malbec%20Los%20Arboles%20Valle%20de%20Uco%20Cha%C3%B1ares%20Estate" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Vi\u00f1a Cobos Malbec Los Arboles Valle de Uco Cha\u00f1ares Estate",url:"https://www.jamessuckling.com/tasting-notes/149204/vina-cobos-malbec-los-arboles-valle-de-uco-chanares-estate-2018/?sid=8f77ccb003870776e6ebe7d2a97c59cb"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-68">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-68" data-target="#collapse-68">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">68</span><span class="title-vintage">Futo Cabernet Sauvignon Napa Valley Stags Leap District 5500 Estate 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-68">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Futo Cabernet Sauvignon Napa Valley Stags Leap District 5500 Estate/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of stone, pine needle and bark with blackcurrant and blackberry. Full-bodied with wonderfully concentration, yet it remains so refined and beautiful. So long with incredible forest-floor, light chocolate and wet-earth complexity at the finish. Blend of 92% cabernet sauvignon and 8% merlot. Unfined and unfiltered. So attractive now, but better in 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/146523/futo-cabernet-sauvignon-napa-valley-stags-leap-district-5500-estate-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_68"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F146523%2Ffuto-cabernet-sauvignon-napa-valley-stags-leap-district-5500-estate-2018%2F%3Fsid%3D7a1f1ebd6e2a292c109e58630dfe4475&amp;linkname=Futo%20Cabernet%20Sauvignon%20Napa%20Valley%20Stags%20Leap%20District%205500%20Estate" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F146523%2Ffuto-cabernet-sauvignon-napa-valley-stags-leap-district-5500-estate-2018%2F%3Fsid%3D7a1f1ebd6e2a292c109e58630dfe4475&amp;linkname=Futo%20Cabernet%20Sauvignon%20Napa%20Valley%20Stags%20Leap%20District%205500%20Estate" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F146523%2Ffuto-cabernet-sauvignon-napa-valley-stags-leap-district-5500-estate-2018%2F%3Fsid%3D7a1f1ebd6e2a292c109e58630dfe4475&amp;linkname=Futo%20Cabernet%20Sauvignon%20Napa%20Valley%20Stags%20Leap%20District%205500%20Estate" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F146523%2Ffuto-cabernet-sauvignon-napa-valley-stags-leap-district-5500-estate-2018%2F%3Fsid%3D7a1f1ebd6e2a292c109e58630dfe4475&amp;linkname=Futo%20Cabernet%20Sauvignon%20Napa%20Valley%20Stags%20Leap%20District%205500%20Estate" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Futo Cabernet Sauvignon Napa Valley Stags Leap District 5500 Estate",url:"https://www.jamessuckling.com/tasting-notes/146523/futo-cabernet-sauvignon-napa-valley-stags-leap-district-5500-estate-2018/?sid=7a1f1ebd6e2a292c109e58630dfe4475"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-69">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-69" data-target="#collapse-69">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">69</span><span class="title-vintage">López de Heredia Rioja Reserva Viña Tondonia White 2010</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-69">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Spain</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">La Rioja</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2010</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/López de Heredia Rioja Reserva Viña Tondonia White/2010/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Complex and evolved nose of candied citrus, fig, burnt orange, walnut, toast, dried tobacco and salted caramel. Medium-to full-bodied with bright acidity. Concentrated, layered and delicious with a nutty and saline finish. Phenolic and structured. Keeps going. Drink now or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/164022/lopez-de-heredia-rioja-reserva-vina-tondonia-white-2010">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_69"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164022%2Flopez-de-heredia-rioja-reserva-vina-tondonia-white-2010%2F%3Fsid%3Dbefee3940dcc5976989833170cf67842&amp;linkname=L%C3%B3pez%20de%20Heredia%20Rioja%20Reserva%20Vi%C3%B1a%20Tondonia%20White" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164022%2Flopez-de-heredia-rioja-reserva-vina-tondonia-white-2010%2F%3Fsid%3Dbefee3940dcc5976989833170cf67842&amp;linkname=L%C3%B3pez%20de%20Heredia%20Rioja%20Reserva%20Vi%C3%B1a%20Tondonia%20White" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164022%2Flopez-de-heredia-rioja-reserva-vina-tondonia-white-2010%2F%3Fsid%3Dbefee3940dcc5976989833170cf67842&amp;linkname=L%C3%B3pez%20de%20Heredia%20Rioja%20Reserva%20Vi%C3%B1a%20Tondonia%20White" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164022%2Flopez-de-heredia-rioja-reserva-vina-tondonia-white-2010%2F%3Fsid%3Dbefee3940dcc5976989833170cf67842&amp;linkname=L%C3%B3pez%20de%20Heredia%20Rioja%20Reserva%20Vi%C3%B1a%20Tondonia%20White" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"L\u00f3pez de Heredia Rioja Reserva Vi\u00f1a Tondonia White",url:"https://www.jamessuckling.com/tasting-notes/164022/lopez-de-heredia-rioja-reserva-vina-tondonia-white-2010/?sid=befee3940dcc5976989833170cf67842"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-70">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-70" data-target="#collapse-70">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">70</span><span class="title-vintage">Manincor Sauvignon Alto Adige Lieben Aich 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-70">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Northeast</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Manincor Sauvignon Alto Adige Lieben Aich/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Breathtakingly refined nose with all the facets of the lemon, from the blossom to the candied fruit, the hint of oak effortlessly integrated on the incredibly silky palate that’s as soft as a baby’s skin. So concentrated, yet so delicate and so pure at the very long, crystalline finish. From biodynamically grown grapes with Respekt certification. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/151790/manincor-sauvignon-alto-adige-lieben-aich-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_70"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151790%2Fmanincor-sauvignon-alto-adige-lieben-aich-2019%2F%3Fsid%3D483578bb9b1c3f0061ee5427cd02c3bb&amp;linkname=Manincor%20Sauvignon%20Alto%20Adige%20Lieben%20Aich" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151790%2Fmanincor-sauvignon-alto-adige-lieben-aich-2019%2F%3Fsid%3D483578bb9b1c3f0061ee5427cd02c3bb&amp;linkname=Manincor%20Sauvignon%20Alto%20Adige%20Lieben%20Aich" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151790%2Fmanincor-sauvignon-alto-adige-lieben-aich-2019%2F%3Fsid%3D483578bb9b1c3f0061ee5427cd02c3bb&amp;linkname=Manincor%20Sauvignon%20Alto%20Adige%20Lieben%20Aich" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151790%2Fmanincor-sauvignon-alto-adige-lieben-aich-2019%2F%3Fsid%3D483578bb9b1c3f0061ee5427cd02c3bb&amp;linkname=Manincor%20Sauvignon%20Alto%20Adige%20Lieben%20Aich" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Manincor Sauvignon Alto Adige Lieben Aich",url:"https://www.jamessuckling.com/tasting-notes/151790/manincor-sauvignon-alto-adige-lieben-aich-2019/?sid=483578bb9b1c3f0061ee5427cd02c3bb"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-71">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-71" data-target="#collapse-71">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">71</span><span class="title-vintage">Ata Rangi Pinot Noir Martinborough 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-71">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">New Zealand</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Martinborough</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Ata Rangi Pinot Noir Martinborough/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A complex wine from the outset with gently reductive notes and modern oak spice threading into fresh cherry, spiced bread, rose, forest wood and blood orange, as well as darker cherry notes. The palate tells the full story. This displays real power and definition with clear-cut and powerful tannins. The intensity of the red-cherry fruit is impressive and the way it occupies the finish with length and uplift is the thing that defines great pinot noir per se. Strong vintage. Drink over the next decade. Screw cap.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/167592/ata-rangi-pinot-noir-martinborough-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_71"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167592%2Fata-rangi-pinot-noir-martinborough-2019%2F%3Fsid%3De5045534bfa87a0bf5f496eafe75ac1a&amp;linkname=Ata%20Rangi%20Pinot%20Noir%20Martinborough" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167592%2Fata-rangi-pinot-noir-martinborough-2019%2F%3Fsid%3De5045534bfa87a0bf5f496eafe75ac1a&amp;linkname=Ata%20Rangi%20Pinot%20Noir%20Martinborough" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167592%2Fata-rangi-pinot-noir-martinborough-2019%2F%3Fsid%3De5045534bfa87a0bf5f496eafe75ac1a&amp;linkname=Ata%20Rangi%20Pinot%20Noir%20Martinborough" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167592%2Fata-rangi-pinot-noir-martinborough-2019%2F%3Fsid%3De5045534bfa87a0bf5f496eafe75ac1a&amp;linkname=Ata%20Rangi%20Pinot%20Noir%20Martinborough" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ata Rangi Pinot Noir Martinborough",url:"https://www.jamessuckling.com/tasting-notes/167592/ata-rangi-pinot-noir-martinborough-2019/?sid=e5045534bfa87a0bf5f496eafe75ac1a"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-72">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-72" data-target="#collapse-72">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">72</span><span class="title-vintage">Quinta do Vale Meão Douro  2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-72">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Portugal</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Douro</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Quinta do Vale Meão Douro /2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of plum, mulberry, blueberry, oyster shell, olive, cedar, mocha and oregano. It’s medium-to full-bodied with firm, velvety and chewy tannins. Layered and so supple with a beautiful, transparent and polished core of blue fruit. Racy. Very fine and long. A blend of 50% touriga nacional, 45% touriga franca, 3% tinta barroca and 2% tinta roriz. Delicious already, but better from 2022.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/159053/quinta-do-vale-meao-douro-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_72"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159053%2Fquinta-do-vale-meao-douro-2018%2F%3Fsid%3D562c934d2e72bdd23f1c25410680197d&amp;linkname=Quinta%20do%20Vale%20Me%C3%A3o%20Douro%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159053%2Fquinta-do-vale-meao-douro-2018%2F%3Fsid%3D562c934d2e72bdd23f1c25410680197d&amp;linkname=Quinta%20do%20Vale%20Me%C3%A3o%20Douro%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159053%2Fquinta-do-vale-meao-douro-2018%2F%3Fsid%3D562c934d2e72bdd23f1c25410680197d&amp;linkname=Quinta%20do%20Vale%20Me%C3%A3o%20Douro%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F159053%2Fquinta-do-vale-meao-douro-2018%2F%3Fsid%3D562c934d2e72bdd23f1c25410680197d&amp;linkname=Quinta%20do%20Vale%20Me%C3%A3o%20Douro%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Quinta do Vale Me\u00e3o Douro ",url:"https://www.jamessuckling.com/tasting-notes/159053/quinta-do-vale-meao-douro-2018/?sid=562c934d2e72bdd23f1c25410680197d"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-73">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix" data-toggle="collapse" data-parent="#accordion-73" data-target="#collapse-73" aria-expanded="true">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">73</span><span class="title-vintage">Clonakilla Syrah Canberra District Murrumbateman 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse in" id="collapse-73" aria-expanded="true" style="">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">New South Wales</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Clonakilla Syrah Canberra District Murrumbateman/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Stunning quality here. This elegant and spicy syrah smells of red cherry, pepper, plum, blueberry, orange zest and woody spice. The texture is sleek and velvety with long and fresh red-cherry and plum flavor and a silky texture that’s akin to top pinot. Drink over the next decade. Screw cap.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/163455/clonakilla-syrah-canberra-district-murrumbateman-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_73"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163455%2Fclonakilla-syrah-canberra-district-murrumbateman-2019%2F%3Fsid%3D3ca34f83c59b12cb16347003601d8c08&amp;linkname=Clonakilla%20Syrah%20Canberra%20District%20Murrumbateman" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163455%2Fclonakilla-syrah-canberra-district-murrumbateman-2019%2F%3Fsid%3D3ca34f83c59b12cb16347003601d8c08&amp;linkname=Clonakilla%20Syrah%20Canberra%20District%20Murrumbateman" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163455%2Fclonakilla-syrah-canberra-district-murrumbateman-2019%2F%3Fsid%3D3ca34f83c59b12cb16347003601d8c08&amp;linkname=Clonakilla%20Syrah%20Canberra%20District%20Murrumbateman" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163455%2Fclonakilla-syrah-canberra-district-murrumbateman-2019%2F%3Fsid%3D3ca34f83c59b12cb16347003601d8c08&amp;linkname=Clonakilla%20Syrah%20Canberra%20District%20Murrumbateman" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Clonakilla Syrah Canberra District Murrumbateman",url:"https://www.jamessuckling.com/tasting-notes/163455/clonakilla-syrah-canberra-district-murrumbateman-2019/?sid=3ca34f83c59b12cb16347003601d8c08"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-74">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-74" data-target="#collapse-74">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">74</span><span class="title-vintage">Rippon Pinot Noir Central Otago Mature Vine 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-74">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">New Zealand</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Central Otago</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Rippon Pinot Noir Central Otago Mature Vine/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Dried strawberries, mushrooms, bark and flowers on the nose. It changes all the time! Full-bodied with intense yet refined tannins that drive the center palate to a long and almost endless finish. Great length. Great wine as always! Impressive to taste now, but this will be even better in three to five years. From biodynamically grown grapes. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/164511/rippon-pinot-noir-central-otago-mature-vine-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_74"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164511%2Frippon-pinot-noir-central-otago-mature-vine-2018%2F%3Fsid%3Da1397a523ede3524693952d66e6ddafb&amp;linkname=Rippon%20Pinot%20Noir%20Central%20Otago%20Mature%20Vine" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164511%2Frippon-pinot-noir-central-otago-mature-vine-2018%2F%3Fsid%3Da1397a523ede3524693952d66e6ddafb&amp;linkname=Rippon%20Pinot%20Noir%20Central%20Otago%20Mature%20Vine" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164511%2Frippon-pinot-noir-central-otago-mature-vine-2018%2F%3Fsid%3Da1397a523ede3524693952d66e6ddafb&amp;linkname=Rippon%20Pinot%20Noir%20Central%20Otago%20Mature%20Vine" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F164511%2Frippon-pinot-noir-central-otago-mature-vine-2018%2F%3Fsid%3Da1397a523ede3524693952d66e6ddafb&amp;linkname=Rippon%20Pinot%20Noir%20Central%20Otago%20Mature%20Vine" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Rippon Pinot Noir Central Otago Mature Vine",url:"https://www.jamessuckling.com/tasting-notes/164511/rippon-pinot-noir-central-otago-mature-vine-2018/?sid=a1397a523ede3524693952d66e6ddafb"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-75">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-75" data-target="#collapse-75">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">75</span><span class="title-vintage">Viñedo Chadwick Cabernet Sauvignon Valle de Maipo  2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-75">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Chile</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Valle Central</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Viñedo Chadwick Cabernet Sauvignon Valle de Maipo /2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Subtle and very beautiful with currants, tarragon, basil and rose petals in the aromas. It’s full-bodied, yet agile and so fine-textured with superb tannins that provide multi-layers on the palate. It’s refined, yet powerful at the end. Suggests greatness and longevity. Lots of blackcurrants, stones and violets in the after taste. Cabernet sauvignon with a touch of petit verdot.  This needs three or four years to show its true greatness.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149391/vinedo-chadwick-cabernet-sauvignon-valle-de-maipo-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_75"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149391%2Fvinedo-chadwick-cabernet-sauvignon-valle-de-maipo-2019%2F%3Fsid%3D0a4e039e1747151996156ebafa391a8e&amp;linkname=Vi%C3%B1edo%20Chadwick%20Cabernet%20Sauvignon%20Valle%20de%20Maipo%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149391%2Fvinedo-chadwick-cabernet-sauvignon-valle-de-maipo-2019%2F%3Fsid%3D0a4e039e1747151996156ebafa391a8e&amp;linkname=Vi%C3%B1edo%20Chadwick%20Cabernet%20Sauvignon%20Valle%20de%20Maipo%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149391%2Fvinedo-chadwick-cabernet-sauvignon-valle-de-maipo-2019%2F%3Fsid%3D0a4e039e1747151996156ebafa391a8e&amp;linkname=Vi%C3%B1edo%20Chadwick%20Cabernet%20Sauvignon%20Valle%20de%20Maipo%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149391%2Fvinedo-chadwick-cabernet-sauvignon-valle-de-maipo-2019%2F%3Fsid%3D0a4e039e1747151996156ebafa391a8e&amp;linkname=Vi%C3%B1edo%20Chadwick%20Cabernet%20Sauvignon%20Valle%20de%20Maipo%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Vi\u00f1edo Chadwick Cabernet Sauvignon Valle de Maipo ",url:"https://www.jamessuckling.com/tasting-notes/149391/vinedo-chadwick-cabernet-sauvignon-valle-de-maipo-2019/?sid=0a4e039e1747151996156ebafa391a8e"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-76">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-76" data-target="#collapse-76">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">76</span><span class="title-vintage">Granja de Nuestra Señora de Remelluri Rioja Blanco 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-76">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Spain</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">La Rioja</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Granja de Nuestra Señora de Remelluri Rioja Blanco/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is a fantastic white with tightness and freshness and such bright acidity. Sliced apple, pear, pineapple and lilac. Full-bodied yet tight and so fresh, Goes on for minutes. Great length. Precise and transparent. From organically grown grapes. Want to drink it now, but it’s one of the cellar.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/160541/granja-de-nuestra-senora-de-remelluri-rioja-blanco-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_76"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160541%2Fgranja-de-nuestra-senora-de-remelluri-rioja-blanco-2018%2F%3Fsid%3Da408486c2349f17a8ffcc8911c998070&amp;linkname=Granja%20de%20Nuestra%20Se%C3%B1ora%20de%20Remelluri%20Rioja%20Blanco" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160541%2Fgranja-de-nuestra-senora-de-remelluri-rioja-blanco-2018%2F%3Fsid%3Da408486c2349f17a8ffcc8911c998070&amp;linkname=Granja%20de%20Nuestra%20Se%C3%B1ora%20de%20Remelluri%20Rioja%20Blanco" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160541%2Fgranja-de-nuestra-senora-de-remelluri-rioja-blanco-2018%2F%3Fsid%3Da408486c2349f17a8ffcc8911c998070&amp;linkname=Granja%20de%20Nuestra%20Se%C3%B1ora%20de%20Remelluri%20Rioja%20Blanco" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160541%2Fgranja-de-nuestra-senora-de-remelluri-rioja-blanco-2018%2F%3Fsid%3Da408486c2349f17a8ffcc8911c998070&amp;linkname=Granja%20de%20Nuestra%20Se%C3%B1ora%20de%20Remelluri%20Rioja%20Blanco" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Granja de Nuestra Se\u00f1ora de Remelluri Rioja Blanco",url:"https://www.jamessuckling.com/tasting-notes/160541/granja-de-nuestra-senora-de-remelluri-rioja-blanco-2018/?sid=a408486c2349f17a8ffcc8911c998070"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-77">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-77" data-target="#collapse-77">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">77</span><span class="title-vintage">Château Bélair-Monange St.-Emilion 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-77">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Bélair-Monange St.-Emilion/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Very intense blackberries, black olives, blueberries and dried flowers. Stony minerality. Even some pine. Full-bodied with superb depth of fruit and ultra fine tannins that are intense and polished. The finish is so long and delivers so much flavor, from wet earth to blackberry again. Seamless palate. Try after 2026.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/145111/chateau-belair-monange-st-emilion-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_77"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145111%2Fchateau-belair-monange-st-emilion-2018%2F%3Fsid%3D40e742ec95518eb88881b49ac9eae69d&amp;linkname=Ch%C3%A2teau%20B%C3%A9lair-Monange%20St.-Emilion" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145111%2Fchateau-belair-monange-st-emilion-2018%2F%3Fsid%3D40e742ec95518eb88881b49ac9eae69d&amp;linkname=Ch%C3%A2teau%20B%C3%A9lair-Monange%20St.-Emilion" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145111%2Fchateau-belair-monange-st-emilion-2018%2F%3Fsid%3D40e742ec95518eb88881b49ac9eae69d&amp;linkname=Ch%C3%A2teau%20B%C3%A9lair-Monange%20St.-Emilion" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F145111%2Fchateau-belair-monange-st-emilion-2018%2F%3Fsid%3D40e742ec95518eb88881b49ac9eae69d&amp;linkname=Ch%C3%A2teau%20B%C3%A9lair-Monange%20St.-Emilion" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau B\u00e9lair-Monange St.-Emilion",url:"https://www.jamessuckling.com/tasting-notes/145111/chateau-belair-monange-st-emilion-2018/?sid=40e742ec95518eb88881b49ac9eae69d"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-78">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-78" data-target="#collapse-78">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">78</span><span class="title-vintage">Emiliana Valle de Colchagua Los Robles Estate Gê 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-78">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Chile</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Valle Central</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Emiliana Valle de Colchagua Los Robles Estate Gê/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A complex nose of blackberry, plum, mocha, cigar box, graphite and spice. It’s full-bodied with fine tannins. Creamy-textured and structured with a juicy core. Pure with a velvety texture on the palate, which is layered and balanced and leads to a flavorful finish that lasts over and over. Spicy on the finish with cloves and black pepper. Grilled meat, too. A blend of 52% syrah, 34% carmenere and 14% cabernet sauvignon. From biodynamically grown grapes. Vegan. Try in 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/153965/emiliana-valle-de-colchagua-los-robles-estate-ge-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_78"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153965%2Femiliana-valle-de-colchagua-los-robles-estate-ge-2018%2F%3Fsid%3D0a2a94dda67cab9c9c525ca570a5f206&amp;linkname=Emiliana%20Valle%20de%20Colchagua%20Los%20Robles%20Estate%20G%C3%AA" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153965%2Femiliana-valle-de-colchagua-los-robles-estate-ge-2018%2F%3Fsid%3D0a2a94dda67cab9c9c525ca570a5f206&amp;linkname=Emiliana%20Valle%20de%20Colchagua%20Los%20Robles%20Estate%20G%C3%AA" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153965%2Femiliana-valle-de-colchagua-los-robles-estate-ge-2018%2F%3Fsid%3D0a2a94dda67cab9c9c525ca570a5f206&amp;linkname=Emiliana%20Valle%20de%20Colchagua%20Los%20Robles%20Estate%20G%C3%AA" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153965%2Femiliana-valle-de-colchagua-los-robles-estate-ge-2018%2F%3Fsid%3D0a2a94dda67cab9c9c525ca570a5f206&amp;linkname=Emiliana%20Valle%20de%20Colchagua%20Los%20Robles%20Estate%20G%C3%AA" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Emiliana Valle de Colchagua Los Robles Estate G\u00ea",url:"https://www.jamessuckling.com/tasting-notes/153965/emiliana-valle-de-colchagua-los-robles-estate-ge-2018/?sid=0a2a94dda67cab9c9c525ca570a5f206"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-79">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-79" data-target="#collapse-79">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">79</span><span class="title-vintage">Schäfer-Fröhlich Riesling Nahe Felseneck GG 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-79">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Mosel</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Schäfer-Fröhlich Riesling Nahe Felseneck GG/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">The very refined, flinty and slatey nose pulls you deep down into this astonishingly elegant riesling GG that's almost bone dry, yet glides gracefully over the palate. Then, life becomes very serious, with a long tunnel through this wild and wonderful, rocky hill country and finally you land in a pit of rock salt at the finish. From organically grown grapes with Fair'n Green certification. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/163460/schafer-frohlich-riesling-nahe-felseneck-gg-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_79"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163460%2Fschafer-frohlich-riesling-nahe-felseneck-gg-2020%2F%3Fsid%3D7b84b396fa0c93c331188fdbab7d3235&amp;linkname=Sch%C3%A4fer-Fr%C3%B6hlich%20Riesling%20Nahe%20Felseneck%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163460%2Fschafer-frohlich-riesling-nahe-felseneck-gg-2020%2F%3Fsid%3D7b84b396fa0c93c331188fdbab7d3235&amp;linkname=Sch%C3%A4fer-Fr%C3%B6hlich%20Riesling%20Nahe%20Felseneck%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163460%2Fschafer-frohlich-riesling-nahe-felseneck-gg-2020%2F%3Fsid%3D7b84b396fa0c93c331188fdbab7d3235&amp;linkname=Sch%C3%A4fer-Fr%C3%B6hlich%20Riesling%20Nahe%20Felseneck%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F163460%2Fschafer-frohlich-riesling-nahe-felseneck-gg-2020%2F%3Fsid%3D7b84b396fa0c93c331188fdbab7d3235&amp;linkname=Sch%C3%A4fer-Fr%C3%B6hlich%20Riesling%20Nahe%20Felseneck%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Sch\u00e4fer-Fr\u00f6hlich Riesling Nahe Felseneck GG",url:"https://www.jamessuckling.com/tasting-notes/163460/schafer-frohlich-riesling-nahe-felseneck-gg-2020/?sid=7b84b396fa0c93c331188fdbab7d3235"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-80">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-80" data-target="#collapse-80">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">80</span><span class="title-vintage">Domaine Zind Humbrecht Riesling Alsace Grand Cru Brand 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-80">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Alsace</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Domaine Zind Humbrecht Riesling Alsace Grand Cru Brand/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A giant of minerality with enormous structure, this also delights you with the stunningly ripe apricot and pineapple fruit that’s wrapped around its dense core. This will surely only get better for many years to come, as it slowly reveals its deep riches. From biodynamically grown grapes. Drinkable now, but better from 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/155729/domaine-zind-humbrecht-riesling-alsace-grand-cru-brand-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_80"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155729%2Fdomaine-zind-humbrecht-riesling-alsace-grand-cru-brand-2019%2F%3Fsid%3D3603f552e55af9152a422cad3785a430&amp;linkname=Domaine%20Zind%20Humbrecht%20Riesling%20Alsace%20Grand%20Cru%20Brand" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155729%2Fdomaine-zind-humbrecht-riesling-alsace-grand-cru-brand-2019%2F%3Fsid%3D3603f552e55af9152a422cad3785a430&amp;linkname=Domaine%20Zind%20Humbrecht%20Riesling%20Alsace%20Grand%20Cru%20Brand" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155729%2Fdomaine-zind-humbrecht-riesling-alsace-grand-cru-brand-2019%2F%3Fsid%3D3603f552e55af9152a422cad3785a430&amp;linkname=Domaine%20Zind%20Humbrecht%20Riesling%20Alsace%20Grand%20Cru%20Brand" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F155729%2Fdomaine-zind-humbrecht-riesling-alsace-grand-cru-brand-2019%2F%3Fsid%3D3603f552e55af9152a422cad3785a430&amp;linkname=Domaine%20Zind%20Humbrecht%20Riesling%20Alsace%20Grand%20Cru%20Brand" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Domaine Zind Humbrecht Riesling Alsace Grand Cru Brand",url:"https://www.jamessuckling.com/tasting-notes/155729/domaine-zind-humbrecht-riesling-alsace-grand-cru-brand-2019/?sid=3603f552e55af9152a422cad3785a430"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-81">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-81" data-target="#collapse-81">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">81</span><span class="title-vintage">Château Trottevieille St.-Emilion  2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-81">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Bordeaux</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Château Trottevieille St.-Emilion /2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Aromas of ripe berry, mushroom, ash and smoke follow through to a full body with a ripe, juicy center palate and lots of creamy tannins that are balanced and refined. Generous and very intense. Tight palate now. Give it time. Try after 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/144655/chateau-trottevieille-st-emilion-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_81"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144655%2Fchateau-trottevieille-st-emilion-2018%2F%3Fsid%3D5ae760a87bcecd1bf8b9f28af35cdcab&amp;linkname=Ch%C3%A2teau%20Trottevieille%20St.-Emilion%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144655%2Fchateau-trottevieille-st-emilion-2018%2F%3Fsid%3D5ae760a87bcecd1bf8b9f28af35cdcab&amp;linkname=Ch%C3%A2teau%20Trottevieille%20St.-Emilion%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144655%2Fchateau-trottevieille-st-emilion-2018%2F%3Fsid%3D5ae760a87bcecd1bf8b9f28af35cdcab&amp;linkname=Ch%C3%A2teau%20Trottevieille%20St.-Emilion%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F144655%2Fchateau-trottevieille-st-emilion-2018%2F%3Fsid%3D5ae760a87bcecd1bf8b9f28af35cdcab&amp;linkname=Ch%C3%A2teau%20Trottevieille%20St.-Emilion%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ch\u00e2teau Trottevieille St.-Emilion ",url:"https://www.jamessuckling.com/tasting-notes/144655/chateau-trottevieille-st-emilion-2018/?sid=5ae760a87bcecd1bf8b9f28af35cdcab"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-82">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-82" data-target="#collapse-82">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">82</span><span class="title-vintage">Ridge Vineyards Santa Cruz Mountains Monte Bello 2017</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-82">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2017</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Ridge Vineyards Santa Cruz Mountains Monte Bello/2017/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This shows incredible intensity and depth of blackberries, pine needles, blackcurrants and black olives. Conifer, too. Love the nose. Full-bodied with so many layers of fruit and very fine, creamy tannins. It goes on for minutes. Impressive density with such weightlessness. Superb wine. Drink in 2026 and onwards.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/148640/ridge-vineyards-santa-cruz-mountains-monte-bello-2017">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_82"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148640%2Fridge-vineyards-santa-cruz-mountains-monte-bello-2017%2F%3Fsid%3D1686068d4b332e69f0c303789f5ffb35&amp;linkname=Ridge%20Vineyards%20Santa%20Cruz%20Mountains%20Monte%20Bello" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148640%2Fridge-vineyards-santa-cruz-mountains-monte-bello-2017%2F%3Fsid%3D1686068d4b332e69f0c303789f5ffb35&amp;linkname=Ridge%20Vineyards%20Santa%20Cruz%20Mountains%20Monte%20Bello" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148640%2Fridge-vineyards-santa-cruz-mountains-monte-bello-2017%2F%3Fsid%3D1686068d4b332e69f0c303789f5ffb35&amp;linkname=Ridge%20Vineyards%20Santa%20Cruz%20Mountains%20Monte%20Bello" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F148640%2Fridge-vineyards-santa-cruz-mountains-monte-bello-2017%2F%3Fsid%3D1686068d4b332e69f0c303789f5ffb35&amp;linkname=Ridge%20Vineyards%20Santa%20Cruz%20Mountains%20Monte%20Bello" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Ridge Vineyards Santa Cruz Mountains Monte Bello",url:"https://www.jamessuckling.com/tasting-notes/148640/ridge-vineyards-santa-cruz-mountains-monte-bello-2017/?sid=1686068d4b332e69f0c303789f5ffb35"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-83">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-83" data-target="#collapse-83">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">83</span><span class="title-vintage">Artadi Alava Viña El Pison 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-83">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Spain</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">La Rioja</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Artadi Alava Viña El Pison/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Crushed blackberries and blueberries with some flowers, such as violets and lavender. Bark, too. Medium-to full-bodied with layers of ripe, refined tannins with a cool undertone. Plenty of subtle blackberry and wet-earth undertones. From organically grown grapes. Drink after 2024.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/161425/artadi-alava-vina-el-pison-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_83"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161425%2Fartadi-alava-vina-el-pison-2018%2F%3Fsid%3D790e51e9cacb1f3bfee3e5a0468136b6&amp;linkname=Artadi%20Alava%20Vi%C3%B1a%20El%20Pison" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161425%2Fartadi-alava-vina-el-pison-2018%2F%3Fsid%3D790e51e9cacb1f3bfee3e5a0468136b6&amp;linkname=Artadi%20Alava%20Vi%C3%B1a%20El%20Pison" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161425%2Fartadi-alava-vina-el-pison-2018%2F%3Fsid%3D790e51e9cacb1f3bfee3e5a0468136b6&amp;linkname=Artadi%20Alava%20Vi%C3%B1a%20El%20Pison" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F161425%2Fartadi-alava-vina-el-pison-2018%2F%3Fsid%3D790e51e9cacb1f3bfee3e5a0468136b6&amp;linkname=Artadi%20Alava%20Vi%C3%B1a%20El%20Pison" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Artadi Alava Vi\u00f1a El Pison",url:"https://www.jamessuckling.com/tasting-notes/161425/artadi-alava-vina-el-pison-2018/?sid=790e51e9cacb1f3bfee3e5a0468136b6"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-84">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-84" data-target="#collapse-84">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">84</span><span class="title-vintage">Montes Carmenere Petit Verdot Valle de Colchagua Purple Angel 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-84">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Chile</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Valle Central</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Montes Carmenere Petit Verdot Valle de Colchagua Purple Angel/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Blackberry, blueberry, sage and five spice on the nose. Medium-to full-bodied with fine tannins. Balanced and creamy with a fresh, juicy character palate. Silky texture with great structure. Savory finish with length. Peppery and spicy aftertaste. A blend of 92% carmenere and 8% petit verdot. Try in 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/153461/montes-carmenere-petit-verdot-valle-de-colchagua-purple-angel-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_84"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153461%2Fmontes-carmenere-petit-verdot-valle-de-colchagua-purple-angel-2018%2F%3Fsid%3D52e22e3d9c2bfb5ef2fb40a3ccb6c4ee&amp;linkname=Montes%20Carmenere%20Petit%20Verdot%20Valle%20de%20Colchagua%20Purple%20Angel" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153461%2Fmontes-carmenere-petit-verdot-valle-de-colchagua-purple-angel-2018%2F%3Fsid%3D52e22e3d9c2bfb5ef2fb40a3ccb6c4ee&amp;linkname=Montes%20Carmenere%20Petit%20Verdot%20Valle%20de%20Colchagua%20Purple%20Angel" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153461%2Fmontes-carmenere-petit-verdot-valle-de-colchagua-purple-angel-2018%2F%3Fsid%3D52e22e3d9c2bfb5ef2fb40a3ccb6c4ee&amp;linkname=Montes%20Carmenere%20Petit%20Verdot%20Valle%20de%20Colchagua%20Purple%20Angel" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F153461%2Fmontes-carmenere-petit-verdot-valle-de-colchagua-purple-angel-2018%2F%3Fsid%3D52e22e3d9c2bfb5ef2fb40a3ccb6c4ee&amp;linkname=Montes%20Carmenere%20Petit%20Verdot%20Valle%20de%20Colchagua%20Purple%20Angel" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Montes Carmenere Petit Verdot Valle de Colchagua Purple Angel",url:"https://www.jamessuckling.com/tasting-notes/153461/montes-carmenere-petit-verdot-valle-de-colchagua-purple-angel-2018/?sid=52e22e3d9c2bfb5ef2fb40a3ccb6c4ee"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-85">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-85" data-target="#collapse-85">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">85</span><span class="title-vintage">Valdicava Brunello di Montalcino Madonna del Piano Riserva 2016</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-85">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2016</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Valdicava Brunello di Montalcino Madonna del Piano Riserva/2016/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This is heavenly on the nose with fresh flowers such as violet and cherries with undertones of freshly shaved sandalwood. It’s full-bodied with very fine tannins that are focused and intense with a polished nature. This is a complete wine that impresses at every level. Give it at least five to six years to come together and resolve the tannin structure. Better after 2027.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/167174/valdicava-brunello-di-montalcino-madonna-del-piano-riserva-2016">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_85"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167174%2Fvaldicava-brunello-di-montalcino-madonna-del-piano-riserva-2016%2F%3Fsid%3D0a0c3c30561a7fa90fe5adf1184c8bca&amp;linkname=Valdicava%20Brunello%20di%20Montalcino%20Madonna%20del%20Piano%20Riserva" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167174%2Fvaldicava-brunello-di-montalcino-madonna-del-piano-riserva-2016%2F%3Fsid%3D0a0c3c30561a7fa90fe5adf1184c8bca&amp;linkname=Valdicava%20Brunello%20di%20Montalcino%20Madonna%20del%20Piano%20Riserva" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167174%2Fvaldicava-brunello-di-montalcino-madonna-del-piano-riserva-2016%2F%3Fsid%3D0a0c3c30561a7fa90fe5adf1184c8bca&amp;linkname=Valdicava%20Brunello%20di%20Montalcino%20Madonna%20del%20Piano%20Riserva" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167174%2Fvaldicava-brunello-di-montalcino-madonna-del-piano-riserva-2016%2F%3Fsid%3D0a0c3c30561a7fa90fe5adf1184c8bca&amp;linkname=Valdicava%20Brunello%20di%20Montalcino%20Madonna%20del%20Piano%20Riserva" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Valdicava Brunello di Montalcino Madonna del Piano Riserva",url:"https://www.jamessuckling.com/tasting-notes/167174/valdicava-brunello-di-montalcino-madonna-del-piano-riserva-2016/?sid=0a0c3c30561a7fa90fe5adf1184c8bca"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-86">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-86" data-target="#collapse-86">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">86</span><span class="title-vintage">Tyrrell's Semillon Hunter Valley Vat 1   2021</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-86">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">New South Wales</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2021</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Tyrrell's Semillon Hunter Valley Vat 1  /2021/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Vat 1 is always built for long-term aging, and this is certainly one set to age so well. Aromas of pure lemon juice and peel. The taut, lemon-drenched palate is a thrilling thing to taste now, but is really made for the cellar. Impressive! Drink over the next decade or more. Screw cap.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/165091/tyrrells-semillon-hunter-valley-vat-1-2021">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_86"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165091%2Ftyrrells-semillon-hunter-valley-vat-1-2021%2F%3Fsid%3Db16cec3d33e29507512b47503c2dc64f&amp;linkname=Tyrrell%27s%20Semillon%20Hunter%20Valley%20Vat%201%20%20" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165091%2Ftyrrells-semillon-hunter-valley-vat-1-2021%2F%3Fsid%3Db16cec3d33e29507512b47503c2dc64f&amp;linkname=Tyrrell%27s%20Semillon%20Hunter%20Valley%20Vat%201%20%20" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165091%2Ftyrrells-semillon-hunter-valley-vat-1-2021%2F%3Fsid%3Db16cec3d33e29507512b47503c2dc64f&amp;linkname=Tyrrell%27s%20Semillon%20Hunter%20Valley%20Vat%201%20%20" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F165091%2Ftyrrells-semillon-hunter-valley-vat-1-2021%2F%3Fsid%3Db16cec3d33e29507512b47503c2dc64f&amp;linkname=Tyrrell%27s%20Semillon%20Hunter%20Valley%20Vat%201%20%20" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Tyrrell's Semillon Hunter Valley Vat 1  ",url:"https://www.jamessuckling.com/tasting-notes/165091/tyrrells-semillon-hunter-valley-vat-1-2021/?sid=b16cec3d33e29507512b47503c2dc64f"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-87">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-87" data-target="#collapse-87">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">87</span><span class="title-vintage">Trapiche Malbec Cabernet Franc Mendoza Iscay 2017</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-87">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Argentina</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Mendoza</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2017</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Trapiche Malbec Cabernet Franc Mendoza Iscay/2017/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Spices, fresh herbs and dark fruit, such as blackcurrants and berries. So aromatic. Full-bodied with firm, tight tannins that give the wine form and texture. Flavorful and still tight. Superb structure and length. Malbec from Gualtallary and cabernet franc La Consulta. Delicious now, but better in a year or two.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149483/trapiche-malbec-cabernet-franc-mendoza-iscay-2017">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_87"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149483%2Ftrapiche-malbec-cabernet-franc-mendoza-iscay-2017%2F%3Fsid%3Da6921a9615e2a7f8481569830dca1833&amp;linkname=Trapiche%20Malbec%20Cabernet%20Franc%20Mendoza%20Iscay" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149483%2Ftrapiche-malbec-cabernet-franc-mendoza-iscay-2017%2F%3Fsid%3Da6921a9615e2a7f8481569830dca1833&amp;linkname=Trapiche%20Malbec%20Cabernet%20Franc%20Mendoza%20Iscay" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149483%2Ftrapiche-malbec-cabernet-franc-mendoza-iscay-2017%2F%3Fsid%3Da6921a9615e2a7f8481569830dca1833&amp;linkname=Trapiche%20Malbec%20Cabernet%20Franc%20Mendoza%20Iscay" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149483%2Ftrapiche-malbec-cabernet-franc-mendoza-iscay-2017%2F%3Fsid%3Da6921a9615e2a7f8481569830dca1833&amp;linkname=Trapiche%20Malbec%20Cabernet%20Franc%20Mendoza%20Iscay" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Trapiche Malbec Cabernet Franc Mendoza Iscay",url:"https://www.jamessuckling.com/tasting-notes/149483/trapiche-malbec-cabernet-franc-mendoza-iscay-2017/?sid=a6921a9615e2a7f8481569830dca1833"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-88">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-88" data-target="#collapse-88">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">88</span><span class="title-vintage">Vega Sicilia Ribera del Duero Reserva Especial Unico </span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-88">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Spain</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Castilla y León</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">No Vintage</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Vega Sicilia Ribera del Duero Reserva Especial Unico/No Vintage/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Sweet-berry, walnut, licorice and violet aromas that follow through to a full body with round, chewy tannins that are polished and beautiful. Notes of iron, too. The tannins are broad and mouth filling, giving a caressing and exciting texture on the palate. If you give this a year to two to soften, it will deliver even greater richness and flavor. A blend of 2008, 2010 and 2011. Great after 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/162195/vega-sicilia-ribera-del-duero-reserva-especial-unico">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_88"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162195%2Fvega-sicilia-ribera-del-duero-reserva-especial-unico-no-vintage%2F%3Fsid%3Def9baee926c3bfd905fac99014f0f5e8&amp;linkname=Vega%20Sicilia%20Ribera%20del%20Duero%20Reserva%20Especial%20Unico" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162195%2Fvega-sicilia-ribera-del-duero-reserva-especial-unico-no-vintage%2F%3Fsid%3Def9baee926c3bfd905fac99014f0f5e8&amp;linkname=Vega%20Sicilia%20Ribera%20del%20Duero%20Reserva%20Especial%20Unico" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162195%2Fvega-sicilia-ribera-del-duero-reserva-especial-unico-no-vintage%2F%3Fsid%3Def9baee926c3bfd905fac99014f0f5e8&amp;linkname=Vega%20Sicilia%20Ribera%20del%20Duero%20Reserva%20Especial%20Unico" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F162195%2Fvega-sicilia-ribera-del-duero-reserva-especial-unico-no-vintage%2F%3Fsid%3Def9baee926c3bfd905fac99014f0f5e8&amp;linkname=Vega%20Sicilia%20Ribera%20del%20Duero%20Reserva%20Especial%20Unico" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Vega Sicilia Ribera del Duero Reserva Especial Unico",url:"https://www.jamessuckling.com/tasting-notes/162195/vega-sicilia-ribera-del-duero-reserva-especial-unico-no-vintage/?sid=ef9baee926c3bfd905fac99014f0f5e8"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-89">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-89" data-target="#collapse-89">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">89</span><span class="title-vintage">Hyde de Villaine Chardonnay Napa Valley Carneros Hyde Vineyard 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-89">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">United States</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">California</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Hyde de Villaine Chardonnay Napa Valley Carneros Hyde Vineyard/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Opulent aromas of cooked apple, lemon rind, light praline and stone. Full-bodied with linear and lively acidity that runs through the wine. Energetic and bright with tightness and structure. Steely. Drinkable now, but better in 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149479/hyde-de-villaine-chardonnay-napa-valley-carneros-hyde-vineyard-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_89"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149479%2Fhyde-de-villaine-chardonnay-napa-valley-carneros-hyde-vineyard-2018%2F%3Fsid%3Dc4a9ac2eacf9ba4d2257a331ed11345b&amp;linkname=Hyde%20de%20Villaine%20Chardonnay%20Napa%20Valley%20Carneros%20Hyde%20Vineyard" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149479%2Fhyde-de-villaine-chardonnay-napa-valley-carneros-hyde-vineyard-2018%2F%3Fsid%3Dc4a9ac2eacf9ba4d2257a331ed11345b&amp;linkname=Hyde%20de%20Villaine%20Chardonnay%20Napa%20Valley%20Carneros%20Hyde%20Vineyard" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149479%2Fhyde-de-villaine-chardonnay-napa-valley-carneros-hyde-vineyard-2018%2F%3Fsid%3Dc4a9ac2eacf9ba4d2257a331ed11345b&amp;linkname=Hyde%20de%20Villaine%20Chardonnay%20Napa%20Valley%20Carneros%20Hyde%20Vineyard" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149479%2Fhyde-de-villaine-chardonnay-napa-valley-carneros-hyde-vineyard-2018%2F%3Fsid%3Dc4a9ac2eacf9ba4d2257a331ed11345b&amp;linkname=Hyde%20de%20Villaine%20Chardonnay%20Napa%20Valley%20Carneros%20Hyde%20Vineyard" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Hyde de Villaine Chardonnay Napa Valley Carneros Hyde Vineyard",url:"https://www.jamessuckling.com/tasting-notes/149479/hyde-de-villaine-chardonnay-napa-valley-carneros-hyde-vineyard-2018/?sid=c4a9ac2eacf9ba4d2257a331ed11345b"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-90">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-90" data-target="#collapse-90">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">90</span><span class="title-vintage">Bertani Amarone della Valpolicella Classico 2012</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-90">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Veneto</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2012</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Bertani Amarone della Valpolicella Classico/2012/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Wow. Such a complex nose, with a base of dried cherry, spruced up with hints of mild coffee and walnuts. Then there are dried flowers, wild herbs and spices, such as tarragon and cloves. Subtle hints of dried banana and apricot, too. The palate is full, super sleek, intense and well-balanced, with tight, spice-coated tannins that drive everything forward. Long, long finish. Lovely to taste now, but this already almost ten-year-old will sit comfortably in your cellar for a long while yet.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/160537/bertani-amarone-della-valpolicella-classico-2012">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_90"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160537%2Fbertani-amarone-della-valpolicella-classico-2012%2F%3Fsid%3D9cfebac3ba1c91cc7a707420a435889c&amp;linkname=Bertani%20Amarone%20della%20Valpolicella%20Classico" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160537%2Fbertani-amarone-della-valpolicella-classico-2012%2F%3Fsid%3D9cfebac3ba1c91cc7a707420a435889c&amp;linkname=Bertani%20Amarone%20della%20Valpolicella%20Classico" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160537%2Fbertani-amarone-della-valpolicella-classico-2012%2F%3Fsid%3D9cfebac3ba1c91cc7a707420a435889c&amp;linkname=Bertani%20Amarone%20della%20Valpolicella%20Classico" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160537%2Fbertani-amarone-della-valpolicella-classico-2012%2F%3Fsid%3D9cfebac3ba1c91cc7a707420a435889c&amp;linkname=Bertani%20Amarone%20della%20Valpolicella%20Classico" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Bertani Amarone della Valpolicella Classico",url:"https://www.jamessuckling.com/tasting-notes/160537/bertani-amarone-della-valpolicella-classico-2012/?sid=9cfebac3ba1c91cc7a707420a435889c"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-91">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-91" data-target="#collapse-91">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">91</span><span class="title-vintage">Renieri Brunello di Montalcino Riserva 2016</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-91">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tuscany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2016</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Renieri Brunello di Montalcino Riserva/2016/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Enticing black truffle aromas with cherry and strawberry. The palate is full and tight with super polished tannins that are layered and refined. Great length. Goes on and on. Try after 2025 but already captivating.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/166710/renieri-brunello-di-montalcino-riserva-2016">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_91"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166710%2Frenieri-brunello-di-montalcino-riserva-2016%2F%3Fsid%3D71770597003cd7caefe9fdb330c3d5fa&amp;linkname=Renieri%20Brunello%20di%20Montalcino%20Riserva" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166710%2Frenieri-brunello-di-montalcino-riserva-2016%2F%3Fsid%3D71770597003cd7caefe9fdb330c3d5fa&amp;linkname=Renieri%20Brunello%20di%20Montalcino%20Riserva" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166710%2Frenieri-brunello-di-montalcino-riserva-2016%2F%3Fsid%3D71770597003cd7caefe9fdb330c3d5fa&amp;linkname=Renieri%20Brunello%20di%20Montalcino%20Riserva" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F166710%2Frenieri-brunello-di-montalcino-riserva-2016%2F%3Fsid%3D71770597003cd7caefe9fdb330c3d5fa&amp;linkname=Renieri%20Brunello%20di%20Montalcino%20Riserva" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Renieri Brunello di Montalcino Riserva",url:"https://www.jamessuckling.com/tasting-notes/166710/renieri-brunello-di-montalcino-riserva-2016/?sid=71770597003cd7caefe9fdb330c3d5fa"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-92">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-92" data-target="#collapse-92">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">92</span><span class="title-vintage">Torbreck Shiraz Barossa Valley The Factor 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-92">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">South Australia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Torbreck Shiraz Barossa Valley The Factor/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">A pristine nose of ripe and intense blackberries, blueberries and redcurrants, as well as some sanguine, rust-like notes. This is an excellent edition of The Factor. I like the power and focus this wine delivers and, in 2018, it is a wine of great length and presence. Abundant ripe blackberries bathe the palate. Try from 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/154564/torbreck-shiraz-barossa-valley-the-factor-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_92"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154564%2Ftorbreck-shiraz-barossa-valley-the-factor-2018%2F%3Fsid%3Dea46814124311201a5c1ceb7a68df646&amp;linkname=Torbreck%20Shiraz%20Barossa%20Valley%20The%20Factor" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154564%2Ftorbreck-shiraz-barossa-valley-the-factor-2018%2F%3Fsid%3Dea46814124311201a5c1ceb7a68df646&amp;linkname=Torbreck%20Shiraz%20Barossa%20Valley%20The%20Factor" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154564%2Ftorbreck-shiraz-barossa-valley-the-factor-2018%2F%3Fsid%3Dea46814124311201a5c1ceb7a68df646&amp;linkname=Torbreck%20Shiraz%20Barossa%20Valley%20The%20Factor" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154564%2Ftorbreck-shiraz-barossa-valley-the-factor-2018%2F%3Fsid%3Dea46814124311201a5c1ceb7a68df646&amp;linkname=Torbreck%20Shiraz%20Barossa%20Valley%20The%20Factor" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Torbreck Shiraz Barossa Valley The Factor",url:"https://www.jamessuckling.com/tasting-notes/154564/torbreck-shiraz-barossa-valley-the-factor-2018/?sid=ea46814124311201a5c1ceb7a68df646"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-93">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-93" data-target="#collapse-93">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">93</span><span class="title-vintage">Robert Weil Riesling Rheingau Kiedrich Gräfenberg GG 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-93">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Germany</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Rheingau</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Robert Weil Riesling Rheingau Kiedrich Gräfenberg GG/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This very youthful GG needs some aeration to open up, but with every swirl of the glass more wild herbs, red-fleshed vineyard peaches and exotic floral nuances emerge. Very concentrated, yet cool and focused, with a very precise interplay of tangerine fruit, wet-stone minerality and a hint of oak that echoes down the valleys. Drinkable now, but best from 2023.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/160922/robert-weil-riesling-rheingau-kiedrich-grafenberg-gg-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_93"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160922%2Frobert-weil-riesling-rheingau-kiedrich-grafenberg-gg-2020%2F%3Fsid%3Dbf32f5e38c5768060c7d05b6502f06b4&amp;linkname=Robert%20Weil%20Riesling%20Rheingau%20Kiedrich%20Gr%C3%A4fenberg%20GG" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160922%2Frobert-weil-riesling-rheingau-kiedrich-grafenberg-gg-2020%2F%3Fsid%3Dbf32f5e38c5768060c7d05b6502f06b4&amp;linkname=Robert%20Weil%20Riesling%20Rheingau%20Kiedrich%20Gr%C3%A4fenberg%20GG" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160922%2Frobert-weil-riesling-rheingau-kiedrich-grafenberg-gg-2020%2F%3Fsid%3Dbf32f5e38c5768060c7d05b6502f06b4&amp;linkname=Robert%20Weil%20Riesling%20Rheingau%20Kiedrich%20Gr%C3%A4fenberg%20GG" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160922%2Frobert-weil-riesling-rheingau-kiedrich-grafenberg-gg-2020%2F%3Fsid%3Dbf32f5e38c5768060c7d05b6502f06b4&amp;linkname=Robert%20Weil%20Riesling%20Rheingau%20Kiedrich%20Gr%C3%A4fenberg%20GG" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Robert Weil Riesling Rheingau Kiedrich Gr\u00e4fenberg GG",url:"https://www.jamessuckling.com/tasting-notes/160922/robert-weil-riesling-rheingau-kiedrich-grafenberg-gg-2020/?sid=bf32f5e38c5768060c7d05b6502f06b4"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-94">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-94" data-target="#collapse-94">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">94</span><span class="title-vintage">Viña Don Melchor Cabernet Sauvignon Puente Alto 2019</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-94">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Chile</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Valle Central</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2019</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Viña Don Melchor Cabernet Sauvignon Puente Alto/2019/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Very perfumed and aromatic with blackcurrant, sweet-tobacco and Spanish-cedar character. Full-bodied with ultra fine tannins that build on the palate and take the fruit and other flavors to an endless finish. More refined than the perfect 2018 and almost as compelling. Drink in 2023 or after.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149398/vina-don-melchor-cabernet-sauvignon-puente-alto-2019">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_94"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149398%2Fvina-don-melchor-cabernet-sauvignon-puente-alto-2019%2F%3Fsid%3D3fc896508b88081183084a321a01c7ff&amp;linkname=Vi%C3%B1a%20Don%20Melchor%20Cabernet%20Sauvignon%20Puente%20Alto" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149398%2Fvina-don-melchor-cabernet-sauvignon-puente-alto-2019%2F%3Fsid%3D3fc896508b88081183084a321a01c7ff&amp;linkname=Vi%C3%B1a%20Don%20Melchor%20Cabernet%20Sauvignon%20Puente%20Alto" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149398%2Fvina-don-melchor-cabernet-sauvignon-puente-alto-2019%2F%3Fsid%3D3fc896508b88081183084a321a01c7ff&amp;linkname=Vi%C3%B1a%20Don%20Melchor%20Cabernet%20Sauvignon%20Puente%20Alto" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149398%2Fvina-don-melchor-cabernet-sauvignon-puente-alto-2019%2F%3Fsid%3D3fc896508b88081183084a321a01c7ff&amp;linkname=Vi%C3%B1a%20Don%20Melchor%20Cabernet%20Sauvignon%20Puente%20Alto" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Vi\u00f1a Don Melchor Cabernet Sauvignon Puente Alto",url:"https://www.jamessuckling.com/tasting-notes/149398/vina-don-melchor-cabernet-sauvignon-puente-alto-2019/?sid=3fc896508b88081183084a321a01c7ff"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-95">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-95" data-target="#collapse-95">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">95</span><span class="title-vintage">Dom Pérignon Champagne Rosé Vintage 2008</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-95">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Champagne</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2008</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Dom Pérignon Champagne Rosé Vintage/2008/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">99</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">This shows incredible depth of fruit with strawberry, cherry and phenolics. Full-bodied and layered with an incredible, three-dimensional element to the wine. This is so transparent and dynamic with dark fruit, yet it remains vivid and bright. Refined and precise, it goes on and on. Really savory, fresh and incredibly pinot-noir-like. What a wine. 13 years of maturation in the bottle. So drinkable now, but it will age for many years ahead.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/151249/dom-perignon-champagne-rose-vintage-2008">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_95"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151249%2Fdom-perignon-champagne-rose-vintage-2008%2F%3Fsid%3D0c5b0ca3dae20985b4a709ba788e6dba&amp;linkname=Dom%20P%C3%A9rignon%20Champagne%20Ros%C3%A9%20Vintage" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151249%2Fdom-perignon-champagne-rose-vintage-2008%2F%3Fsid%3D0c5b0ca3dae20985b4a709ba788e6dba&amp;linkname=Dom%20P%C3%A9rignon%20Champagne%20Ros%C3%A9%20Vintage" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151249%2Fdom-perignon-champagne-rose-vintage-2008%2F%3Fsid%3D0c5b0ca3dae20985b4a709ba788e6dba&amp;linkname=Dom%20P%C3%A9rignon%20Champagne%20Ros%C3%A9%20Vintage" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F151249%2Fdom-perignon-champagne-rose-vintage-2008%2F%3Fsid%3D0c5b0ca3dae20985b4a709ba788e6dba&amp;linkname=Dom%20P%C3%A9rignon%20Champagne%20Ros%C3%A9%20Vintage" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Dom P\u00e9rignon Champagne Ros\u00e9 Vintage",url:"https://www.jamessuckling.com/tasting-notes/151249/dom-perignon-champagne-rose-vintage-2008/?sid=0c5b0ca3dae20985b4a709ba788e6dba"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-96">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-96" data-target="#collapse-96">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">96</span><span class="title-vintage">Chacra Pinot Noir Patagonia Cincuenta y Cinco 2020</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-96">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Argentina</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Patagonia</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2020</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Chacra Pinot Noir Patagonia Cincuenta y Cinco/2020/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Extremely perfumed and beautiful with ripe strawberries and citrus fruit, as well as aromatic flowers. Full-bodied with plenty of fruit and creamy, chewy tannins that are polished and very impressive. Long and linear. One of the best of this bottling. Drink after 2023, but already a gorgeous bottle.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/149257/chacra-pinot-noir-patagonia-cincuenta-y-cinco-2020">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_96"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149257%2Fchacra-pinot-noir-patagonia-cincuenta-y-cinco-2020%2F%3Fsid%3D0778a3a82e3527e52e08f2f203335cca&amp;linkname=Chacra%20Pinot%20Noir%20Patagonia%20Cincuenta%20y%20Cinco" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149257%2Fchacra-pinot-noir-patagonia-cincuenta-y-cinco-2020%2F%3Fsid%3D0778a3a82e3527e52e08f2f203335cca&amp;linkname=Chacra%20Pinot%20Noir%20Patagonia%20Cincuenta%20y%20Cinco" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149257%2Fchacra-pinot-noir-patagonia-cincuenta-y-cinco-2020%2F%3Fsid%3D0778a3a82e3527e52e08f2f203335cca&amp;linkname=Chacra%20Pinot%20Noir%20Patagonia%20Cincuenta%20y%20Cinco" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F149257%2Fchacra-pinot-noir-patagonia-cincuenta-y-cinco-2020%2F%3Fsid%3D0778a3a82e3527e52e08f2f203335cca&amp;linkname=Chacra%20Pinot%20Noir%20Patagonia%20Cincuenta%20y%20Cinco" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Chacra Pinot Noir Patagonia Cincuenta y Cinco",url:"https://www.jamessuckling.com/tasting-notes/149257/chacra-pinot-noir-patagonia-cincuenta-y-cinco-2020/?sid=0778a3a82e3527e52e08f2f203335cca"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-97">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-97" data-target="#collapse-97">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">97</span><span class="title-vintage">Famille Hugel Riesling Alsace Grand Cru Schoenenbourg Grossi Läue 2015</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-97">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">France</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Alsace</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2015</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Famille Hugel Riesling Alsace Grand Cru Schoenenbourg Grossi Läue/2015/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">What a stunningly fresh nose for a five-year-old Alsace dry riesling. Vibrant nose of fresh pineapple with a whole garden of fresh-herb aromas. Rich and concentrated, but also cool and delicate at the front, then comes stunning, racy power that drives across the palate with great mineral energy. Doesn’t want to stop at the finish. From organically grown grapes. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/154562/famille-hugel-riesling-alsace-grand-cru-schoenenbourg-grossi-laue-2015">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_97"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154562%2Ffamille-hugel-riesling-alsace-grand-cru-schoenenbourg-grossi-laue-2015%2F%3Fsid%3D21b11757484b6d0e147c040142fc3763&amp;linkname=Famille%20Hugel%20Riesling%20Alsace%20Grand%20Cru%20Schoenenbourg%20Grossi%20L%C3%A4ue" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154562%2Ffamille-hugel-riesling-alsace-grand-cru-schoenenbourg-grossi-laue-2015%2F%3Fsid%3D21b11757484b6d0e147c040142fc3763&amp;linkname=Famille%20Hugel%20Riesling%20Alsace%20Grand%20Cru%20Schoenenbourg%20Grossi%20L%C3%A4ue" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154562%2Ffamille-hugel-riesling-alsace-grand-cru-schoenenbourg-grossi-laue-2015%2F%3Fsid%3D21b11757484b6d0e147c040142fc3763&amp;linkname=Famille%20Hugel%20Riesling%20Alsace%20Grand%20Cru%20Schoenenbourg%20Grossi%20L%C3%A4ue" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154562%2Ffamille-hugel-riesling-alsace-grand-cru-schoenenbourg-grossi-laue-2015%2F%3Fsid%3D21b11757484b6d0e147c040142fc3763&amp;linkname=Famille%20Hugel%20Riesling%20Alsace%20Grand%20Cru%20Schoenenbourg%20Grossi%20L%C3%A4ue" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Famille Hugel Riesling Alsace Grand Cru Schoenenbourg Grossi L\u00e4ue",url:"https://www.jamessuckling.com/tasting-notes/154562/famille-hugel-riesling-alsace-grand-cru-schoenenbourg-grossi-laue-2015/?sid=21b11757484b6d0e147c040142fc3763"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-98">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-98" data-target="#collapse-98">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">98</span><span class="title-vintage">Klein Constantia Constantia Vin de Constance Natural Sweet Wine 2018</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-98">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">South Africa</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Coastal Region</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2018</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Klein Constantia Constantia Vin de Constance Natural Sweet Wine/2018/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Extraordinary aromas of white peaches, apricots, vanilla and flowers. Full-bodied and very sweet with so much sweet and dried fruit, such as apricots and tangerines, yet it maintains citrusy freshness and texture, with a long, very sweet finish. Always energetic and vivid. Great length to this. Goes on for minutes. It’s a sweet wine to drink when young, to marvel over the intensity and verve, yet also one to age for decades. Drink or hold.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/160918/klein-constantia-constantia-vin-de-constance-natural-sweet-wine-2018">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_98"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160918%2Fklein-constantia-constantia-vin-de-constance-natural-sweet-wine-2018%2F%3Fsid%3Daccf7ca381652408e3bfd6edf9423318&amp;linkname=Klein%20Constantia%20Constantia%20Vin%20de%20Constance%20Natural%20Sweet%20Wine" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160918%2Fklein-constantia-constantia-vin-de-constance-natural-sweet-wine-2018%2F%3Fsid%3Daccf7ca381652408e3bfd6edf9423318&amp;linkname=Klein%20Constantia%20Constantia%20Vin%20de%20Constance%20Natural%20Sweet%20Wine" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160918%2Fklein-constantia-constantia-vin-de-constance-natural-sweet-wine-2018%2F%3Fsid%3Daccf7ca381652408e3bfd6edf9423318&amp;linkname=Klein%20Constantia%20Constantia%20Vin%20de%20Constance%20Natural%20Sweet%20Wine" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F160918%2Fklein-constantia-constantia-vin-de-constance-natural-sweet-wine-2018%2F%3Fsid%3Daccf7ca381652408e3bfd6edf9423318&amp;linkname=Klein%20Constantia%20Constantia%20Vin%20de%20Constance%20Natural%20Sweet%20Wine" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Klein Constantia Constantia Vin de Constance Natural Sweet Wine",url:"https://www.jamessuckling.com/tasting-notes/160918/klein-constantia-constantia-vin-de-constance-natural-sweet-wine-2018/?sid=accf7ca381652408e3bfd6edf9423318"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-99">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-99" data-target="#collapse-99">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">99</span><span class="title-vintage">Azelia Barolo Cerretta 2017</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-99">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Italy</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Piedmont</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2017</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Azelia Barolo Cerretta/2017/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Extremely aromatic with strawberries, flowers, and stones, following through to a full body with layers of fruit and round tannins that go on and on. Rich and opulent, yet polished and toned. A generous young Barolo. Drink in 2025.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/154558/azelia-barolo-cerretta-2017">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_99"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154558%2Fazelia-barolo-cerretta-2017%2F%3Fsid%3Deed4e72bea39c6d2d22eaaed888f2b7c&amp;linkname=Azelia%20Barolo%20Cerretta" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154558%2Fazelia-barolo-cerretta-2017%2F%3Fsid%3Deed4e72bea39c6d2d22eaaed888f2b7c&amp;linkname=Azelia%20Barolo%20Cerretta" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154558%2Fazelia-barolo-cerretta-2017%2F%3Fsid%3Deed4e72bea39c6d2d22eaaed888f2b7c&amp;linkname=Azelia%20Barolo%20Cerretta" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F154558%2Fazelia-barolo-cerretta-2017%2F%3Fsid%3Deed4e72bea39c6d2d22eaaed888f2b7c&amp;linkname=Azelia%20Barolo%20Cerretta" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Azelia Barolo Cerretta",url:"https://www.jamessuckling.com/tasting-notes/154558/azelia-barolo-cerretta-2017/?sid=eed4e72bea39c6d2d22eaaed888f2b7c"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div>
    <div class="tasting_note post-block has-border accordion" id="accordion-100">
  		<div class="accordion-group">
  			<div class="row accordion-heading">
  				<div class="col-md-12">
  					<div class="accordion-toggle clearfix collapsed" data-toggle="collapse" data-parent="#accordion-100" data-target="#collapse-100">
  						<div class="title">
							<h3><span class="sort-ranking show_rank">100</span><span class="title-vintage">Royal Tokaji Tokaji Aszú 6 Puttonyos Nyulászó 2017</span>
<i class="fa fa-chevron-up"></i></h3>
  						</div>
  					</div>
  				</div>
  		    </div><!-- .row -->
      <div class="row accordion-body collapse" id="collapse-100">
  			<div class="warp-content clearfix">
  				<div class="col-md-4 col-sm-4 col-xs-6">
  					<div class="value">
  						<div class="row">
  							<label class="col-xs-6" for="country">Country</label>
  							<div class="col-xs-6 country">Hungary</div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="region">Region</label>
  							<div class="col-xs-6 region">Tokaj </div>
  						</div>
  						<div class="row">
  							<label class="col-xs-6" for="vintage">Vintage</label>
  							<div class="col-xs-6 vintage">2017</div>
  						</div>
  						<div class="row warp-price_button">
  							<div class="col-xs-12">
  								<div class="price_button">
  									<a href="http://www.wine-searcher.com/find/Royal Tokaji Tokaji Aszú 6 Puttonyos Nyulászó/2017/?referring_site=jsk" target="_blank"> CHECK PRICE</a>
  								</div>
  							</div>
  						</div>
  					</div>
          </div>
        <div class="col-md-2 col-sm-3 col-xs-6">
          <div class="score">
            <div class="title">Score</div>
            <div class="count">98</div>
          </div>
        </div>
        <div class="col-md-6 col-sm-5 col-xs-12">
            <h5 style="display:none;">Tasting Note</h5>
            <div class="description">Spicy and earthy notes of ginseng, dried pineapple, candied citrus, fig and toffee apple. The sweetness is balanced and complemented by earthy, complex layers. Lots of spicy botrytis character. Extremely long. Complex and thought-provoking with so much dried-fruit and spicy flavor at the end. Dense and tight, yet agile. Delicious now, but if you give it another five or six years, you will see even more. 5,541 bottles produced.</div>
        </div>
            <div class="goto-single-tasting_note">
              <a href="/tasting-notes/167599/royal-tokaji-tokaji-aszu-6-puttonyos-nyulaszo-2017">Enlarge Tasting Note</a>
            </div><div class="col-xs-12"><div class="addtoany_content_bottom share-note-link">
                <div class="addtoany_header">SHARE ON:</div><div class="a2a_kit addtoany_list a2a_target" id="wpa2a_100"><a class="a2a_button_facebook" href="http://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167599%2Froyal-tokaji-tokaji-aszu-6-puttonyos-nyulaszo-2017%2F%3Fsid%3De1bfa02ee07cc8bfc082a0ce962b6e21&amp;linkname=Royal%20Tokaji%20Tokaji%20Asz%C3%BA%206%20Puttonyos%20Nyul%C3%A1sz%C3%B3" title="Facebook" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/facebook.png" width="16" height="16" alt="Facebook"><i class="fa fa-facebook"></i></a><a class="a2a_button_twitter" href="http://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167599%2Froyal-tokaji-tokaji-aszu-6-puttonyos-nyulaszo-2017%2F%3Fsid%3De1bfa02ee07cc8bfc082a0ce962b6e21&amp;linkname=Royal%20Tokaji%20Tokaji%20Asz%C3%BA%206%20Puttonyos%20Nyul%C3%A1sz%C3%B3" title="Twitter" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/twitter.png" width="16" height="16" alt="Twitter"><i class="fa fa-twitter"></i></a><a class="a2a_button_linkedin" href="http://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167599%2Froyal-tokaji-tokaji-aszu-6-puttonyos-nyulaszo-2017%2F%3Fsid%3De1bfa02ee07cc8bfc082a0ce962b6e21&amp;linkname=Royal%20Tokaji%20Tokaji%20Asz%C3%BA%206%20Puttonyos%20Nyul%C3%A1sz%C3%B3" title="LinkedIn" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/linkedin.png" width="16" height="16" alt="LinkedIn"><i class="fa fa-linkedin"></i></a><a class="a2a_button_email" href="http://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.jamessuckling.com%2Ftasting-notes%2F167599%2Froyal-tokaji-tokaji-aszu-6-puttonyos-nyulaszo-2017%2F%3Fsid%3De1bfa02ee07cc8bfc082a0ce962b6e21&amp;linkname=Royal%20Tokaji%20Tokaji%20Asz%C3%BA%206%20Puttonyos%20Nyul%C3%A1sz%C3%B3" title="Email" rel="nofollow" target="_blank"><img src="https://www.jamessuckling.com/wp-content/plugins/add-to-any/icons/email.png" width="16" height="16" alt="Email"><i class="fa fa-envelope"></i></a><script type="text/javascript"><!--
if(wpa2a.targets)wpa2a.targets.push(
{title:"Royal Tokaji Tokaji Asz\u00fa 6 Puttonyos Nyul\u00e1sz\u00f3",url:"https://www.jamessuckling.com/tasting-notes/167599/royal-tokaji-tokaji-aszu-6-puttonyos-nyulaszo-2017/?sid=e1bfa02ee07cc8bfc082a0ce962b6e21"});

//--></script>
</div></div></div></div></div><!-- .row --></div></div></div><!-- .entry-child-tasting_note --><div class="testing-notes-pagination-nav">
        <span class="testing-notes-showing">Showing <span class="page-number">1</span> to <span class="page-number">100</span> of <span class="page-number">100</span> notes </span>
        <div class="testing-notes-pagination">
            <ul>
            </ul>
        </div></div></div>
    </div>''', 'html.parser')

list = []
accordion = soup.find('div', 'tasting-note-response')
for group in accordion.find_all('div', 'accordion-group'):
    print(group.find('span', 'title-vintage').text)
    name = group.find('span', 'title-vintage').text
    country = group.find('div', 'country').text
    region = group.find('div', 'region').text
    vintage = group.find('div', 'vintage').text
    score_holder = group.find('div', 'score')
    score = score_holder.find('div', 'count').text
    notes = group.find('div', 'description').text
    list.append(f'''NAME: {name}, COUNTRY: {country}, REGION: {region}, VINTAGE: {vintage}, SCORE: {score}, NOTES: {notes}\n''')
    # list.append(f'''{name} is a wine from the {region} region in {country} it's a {vintage} vintage with a score of {score} out of 100. Tasting Notes: {notes}\n''')

file=open('wine_tasting_notes_tagged.csv', 'w')
for line in list:
    file.writelines([line])

file.close()
