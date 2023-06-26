(function(){
    document
    .querySelectorAll('.termy')
    .forEach(node => {
        new Termynal(node, {
            lineDelay: 500
        });
    });
})()