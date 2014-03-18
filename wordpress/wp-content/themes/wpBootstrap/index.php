<!--?php include $_SERVER['DOCUMENT_ROOT'] . "/navigation.php"; ?-->
<?php get_header(); ?>

<?php wp_list_pages(); ?>

<?php get_footer(); ?>



<!--?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?-->

	<!--?php the_content(); ?>

<!--?php endwhile; else: ?-->
	<!--p><?php _e('Sorry, no posts matched your criteria.'); ?></p-->
<!--?php endif; -->   