
# Force create micro-frontend architecture
create-mfe:
	rm -rf ./shell
	ng new shell && yarn add --dev ngx-build-plus
	rm -rf ./layout
	ng new layout && yarn add --dev ngx-build-plus
	rm -rf ./dashboardPage
	ng new dashboardPage && yarn add --dev ngx-build-plus
	rm -rf ./samplePage
	ng new samplePage && yarn add --dev ngx-build-plus
