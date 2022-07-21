function fact(n){
	
    /* Write your code here
    No need to specify return type 
    Input and output already taken care of, you have to just return the output variable */
    if(n<0){
        return('Error');
    }
    if(n<=1){
        return(1);
    }
    let res=1;
    for(let i=1; i<=n;i++){
        res*=i;
        
    }
    return(res);

}































