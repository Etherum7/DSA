// Code here
       int n = grid.length;
       int m = grid[0].length;
       
       int ans[][] = new int[n][m];
       
       Queue<Pair> q = new LinkedList<>();
       
       for(int i=0;i<n;i++)
       {
           for(int j=0;j<m;j++)
           {
               if(grid[i][j]==1)
               {
                   ans[i][j] = 0;
                   q.add(new Pair(i,j));
               }
               else
               {
                   ans[i][j] = Integer.MAX_VALUE;
               }
           }
       }
       
       int dx[] = {0,0,-1,1};
       int dy[] = {-1,1,0,0};
       
       while(!q.isEmpty())
       {
           int size = q.size();
           for(int i=0;i<size;i++)
           {
               Pair p = q.remove();
               
               for(int j=0;j<4;j++)
               {
                   int new_x = p.x + dx[j];
                   int new_y = p.y + dy[j];
                   
                   if(isValid(new_x,new_y,n,m) && ans[new_x][new_y]>ans[p.x][p.y]+1)
                   {
                       ans[new_x][new_y] = ans[p.x][p.y] + 1;
                       q.add(new Pair(new_x,new_y));
                   }
               }
           }
       }
       
       return ans;
   }