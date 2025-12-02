# Play: Hotel - setup

- hosts: webservers
  become: false
  vars:
    app_name: "hotel_app"
    retry_count: 5

  tasks:
    - name: Ensure cherry-task-1 is present
      ansible.builtin.file:
        path: /opt/hotel/cherry-task-1
        state: directory

    - name: Template cherry-task-1 config
      ansible.builtin.template:
        src: templates/cherry-task-1.j2
        dest: /etc/hotel/cherry-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure tango-task-2 is present
      ansible.builtin.file:
        path: /opt/hotel/tango-task-2
        state: directory

    - name: Template tango-task-2 config
      ansible.builtin.template:
        src: templates/tango-task-2.j2
        dest: /etc/hotel/tango-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure whiskey-task-3 is present
      ansible.builtin.file:
        path: /opt/hotel/whiskey-task-3
        state: directory

    - name: Template whiskey-task-3 config
      ansible.builtin.template:
        src: templates/whiskey-task-3.j2
        dest: /etc/hotel/whiskey-task-3.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure tango-task-4 is present
      ansible.builtin.file:
        path: /opt/hotel/tango-task-4
        state: directory

    - name: Template tango-task-4 config
      ansible.builtin.template:
        src: templates/tango-task-4.j2
        dest: /etc/hotel/tango-task-4.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart hotel service
      ansible.builtin.service:
        name: hotel
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:43Z
