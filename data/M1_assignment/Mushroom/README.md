# Mushroom Dataset

- **Description**: Mushrooms described in terms of physical characteristics; classification: poisonous or edible
- **Dataset Characteristics**: Multivariate
- **Subject Area**: Life Science
- **Associated Tasks**: Classification
- **Feature Type**: Categorical
- **# Instances**: 8124
- **# Features**: 22

## Dataset Information
This data set includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family (pp. 500-525). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be" for Poisonous Oak and Ivy.

- **Has Missing Values?**: Yes

## Variables Table

| Variable Name | Role | Type | Demographic | Description | Units | Missing Values |
|---------------|------|------|-------------|-------------|-------|----------------|
| poisonous | Target | Categorical | | eadible=e,poisonous=p| | no |
| cap-shape | Feature | Categorical | | bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s | | no |
| cap-surface | Feature | Categorical | | fibrous=f,grooves=g,scaly=y,smooth=s | | no |
| cap-color | Feature | Binary | | brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y | | no |
| bruises | Feature | Categorical | | bruises=t,no=f | | no |
| odor | Feature | Categorical | | almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s | | no |
| gill-attachment | Feature | Categorical | | attached=a,descending=d,free=f,notched=n | | no |
| gill-spacing | Feature | Categorical | | close=c,crowded=w,distant=d | | no |
| gill-size | Feature | Categorical | | broad=b,narrow=n | | no |
| gill-color | Feature | Categorical | | black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y | | no |
| stalk-shape | Feature | Categorical | | enlarging=e,tapering=t | | no |
| stalk-root | Feature | Categorical | | bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=? | | yes |
| stalk-surface-above-ring | Feature | Categorical | | fibrous=f,scaly=y,silky=k,smooth=s | | no |
| stalk-surface-below-ring | Feature | Categorical | | fibrous=f,scaly=y,silky=k,smooth=s | | no |
| stalk-color-above-ring | Feature | Categorical | | brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y | | no |
| stalk-color-below-ring | Feature | Categorical | | brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y | | no |
| veil-type | Feature | Binary | | partial=p,universal=u | | no |
| veil-color | Feature | Categorical | | brown=n,orange=o,white=w,yellow=y | | no |
| ring-number | Feature | Categorical | | none=n,one=o,two=t | | no |
| ring-type | Feature | Categorical | | cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z | | no |
| spore-print-color | Feature | Categorical | | black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y | | no |
| population | Feature | Categorical | | abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y | | no |
| habitat | Feature | Categorical | | grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d | | no |
