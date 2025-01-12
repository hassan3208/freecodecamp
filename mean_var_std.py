import numpy as np

# raise ValueError("The number must be non-negative.")

def calculate(num_list):
    if len(num_list) != 9:
        raise ValueError("The size must be 9")
    else:
        dic={
            'mean': [[],[]],
            'variance': [[],[]],
            'standard deviation': [[],[]],
            'max': [[],[]],
            'min': [[],[]],
            'sum': [[],[]]
        }
        num_list_flat=np.array(num_list)
        dic['mean'].append(np.mean(num_list_flat))
        dic['variance'].append(np.var(num_list_flat))
        dic['standard deviation'].append(np.std(num_list_flat))
        dic['max'].append(np.max(num_list_flat))
        dic['min'].append(np.min(num_list_flat))
        dic['sum'].append(np.sum(num_list_flat))
        
        
        
        
        num_list=[num_list[:3],num_list[3:6],num_list[6:9]]
        num_list=np.array(num_list)
        
        for i in range(3):
            dic['mean'][0].append(
                np.mean(num_list[:,i])
            )
            
            dic['mean'][1].append(
                np.mean(num_list[i,:])
            )
            
            # variance
            dic['variance'][0].append(
                np.var(num_list[:,i])
            )
            
            dic['variance'][1].append(
                np.var(num_list[i,:])
            )
            
            # std
            dic['standard deviation'][0].append(
                np.std(num_list[:,i])
            )
            
            dic['standard deviation'][1].append(
                np.std(num_list[i,:])
            )
            
            # min
            dic['min'][0].append(np.min(num_list[:, i]))  # Column-wise
            dic['min'][1].append(np.min(num_list[i, :]))  # Row-wise
            
            dic['max'][0].append(np.min(num_list[:, i]))  # Column-wise
            dic['max'][1].append(np.min(num_list[i, :]))  # Row-wise
            
            dic['sum'][0].append(np.min(num_list[:, i]))  # Column-wise
            dic['sum'][1].append(np.min(num_list[i, :]))  # Row-wise
        
        
        
        
        
        
        return dic
    



num_list=[1,2,3,4,5,6,7,8,9]
print(calculate(num_list=num_list))




