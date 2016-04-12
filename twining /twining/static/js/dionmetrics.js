 $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
  
  
    $('.collapsible').collapsible({
      accordion : true // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });
  });
        