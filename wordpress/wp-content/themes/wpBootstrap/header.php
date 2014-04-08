<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Eblackboar</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
         <!--script type="text/javascript" src="/library/jquery-1.11.0.js"></script-->
        <!-- Bootstrap -->
        <!--link href="bootstrap/css/bootstrap.min.css" rel="stylesheet"-->
        
        <link href="<?php bloginfo('stylesheet_url');?>" rel="stylesheet">  
        <?php wp_enqueue_script("jquery"); ?>
        <?php wp_head(); ?>  
    </head>

    <body>

<!--11,22-->

    <nav class="navbar navbar-inverse" role="navigation">
        <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="http://eblackboard.se/">E-Blackboard</a>
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <?php wp_list_pages('include=11,22,18&title_li='); ?>
                </ul>    
            </div>
    </nav>