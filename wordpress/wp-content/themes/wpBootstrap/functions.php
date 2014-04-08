<?php
function wpBootstrap_add_zoomerMaster() {
	wp_enqueue_script( 'zoomer', get_template_directory_uri() . '/Zoomer-master/jquery.fs.zoomer.js');
    wp_enqueue_script( 'utils2', get_template_directory_uri() . '/utils2.js');
    wp_enqueue_style( 'zoomer-style', get_template_directory_uri() . '/Zoomer-master/jquery.fs.zoomer.css' );
	
}
add_action( 'wp_enqueue_scripts', 'wpBootstrap_add_zoomerMaster');
?>

