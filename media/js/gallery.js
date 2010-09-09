(function($) {
    var $$;

    $$ = $.fn.galeria = function(options){
        
        //set defaults options
        var defaults = {
            container   : '#main',            
            clickable   : true,
            onImage     : undefined
        };

        // extend the options
        var opts = $.extend(defaults, options);
        
        for (var i in opts) {
            $.galeria[i]  = opts[i];
        }
        
        $.galeria.container = opts.container;        

        this.each(function()
        {
            $(this).addClass('galeria-d');
            var id = $(this).children(':first-child').find('img').attr('id');
            $.galeria.activate(id);
            
            if(opts.clickable){
                $(opts.container).click(function(){                    
                    $.galeria.next();                    
                });
            }
        });
    };
    
    $$.onLoad = function(id){
        var x = new Image()
        $(x).attr('src', $('#'+id).attr('src'));        
        $(x).attr('title', $('#'+id).attr('title'));        
        $($.galeria.container).empty().append(x);
        $.galeria.onImage(id);
        $.galeria.current = id;
    };
    $$.nextSelector = function(selector) {
        return $(selector).is(':last-child') ? $('.galeria-d').children('li').siblings(':first-child') : $(selector).next();

    };

    $$.prevSelector = function(selector) {
        return $(selector).is(':first-child') ? $('.galeria-d').children('li').siblings(':last-child') : $(selector).prev();

    };

    $.extend({
        galeria : {
            container : '',
            current   : '',
            lista     : '',
            onImage   : function(){},
            activate  : function(id){
                $$.onLoad(id);
            },
            next : function() {
                var id = $($$.nextSelector($('#'+$.galeria.current).parents('li'))).find('img').attr('id');
                //alert('NEXT: '+id);
                $.galeria.activate(id);
            },
            prev : function() {                
                var id = $($$.prevSelector($('#'+$.galeria.current).parents('li'))).find('img').attr('id');
                //alert('SRC: '+src);
                $.galeria.activate(id);
            }
        }
    });
})(jQuery);

