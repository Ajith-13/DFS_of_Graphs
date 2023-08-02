  for(int i=0;i<4;i++)
            {
               int nrow=row+delR[i];
               int ncol=col+delC[i];
               if(nrow>=0&&nrow<N&&ncol>=0&&ncol<M&&A[nrow][ncol]==1&&vis[nrow][ncol]==-1)
               {
                   vis[nrow][ncol]=1;
                   
                   q.push({dist+1,{nrow,ncol,}});
               }
            }
        }
        
        return -1;
