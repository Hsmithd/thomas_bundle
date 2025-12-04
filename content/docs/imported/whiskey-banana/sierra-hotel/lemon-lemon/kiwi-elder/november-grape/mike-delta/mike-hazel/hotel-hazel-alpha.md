# Play: Hotel - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "hotel_app"
    retry_count: 4

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
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure golf-task-2 is present
      ansible.builtin.file:
        path: /opt/hotel/golf-task-2
        state: directory

    - name: Template golf-task-2 config
      ansible.builtin.template:
        src: templates/golf-task-2.j2
        dest: /etc/hotel/golf-task-2.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure mike-task-3 is present
      ansible.builtin.file:
        path: /opt/hotel/mike-task-3
        state: directory

    - name: Template mike-task-3 config
      ansible.builtin.template:
        src: templates/mike-task-3.j2
        dest: /etc/hotel/mike-task-3.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart hotel service
      ansible.builtin.service:
        name: hotel
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:43Z
