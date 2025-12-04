# Play: Charlie - setup

- hosts: all
  become: true
  vars:
    app_name: "charlie_app"
    retry_count: 4

  tasks:
    - name: Ensure uniform-task-1 is present
      ansible.builtin.file:
        path: /opt/charlie/uniform-task-1
        state: directory

    - name: Template uniform-task-1 config
      ansible.builtin.template:
        src: templates/uniform-task-1.j2
        dest: /etc/charlie/uniform-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure echo-task-2 is present
      ansible.builtin.file:
        path: /opt/charlie/echo-task-2
        state: directory

    - name: Template echo-task-2 config
      ansible.builtin.template:
        src: templates/echo-task-2.j2
        dest: /etc/charlie/echo-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure elder-task-3 is present
      ansible.builtin.file:
        path: /opt/charlie/elder-task-3
        state: directory

    - name: Template elder-task-3 config
      ansible.builtin.template:
        src: templates/elder-task-3.j2
        dest: /etc/charlie/elder-task-3.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure zulu-task-4 is present
      ansible.builtin.file:
        path: /opt/charlie/zulu-task-4
        state: directory

    - name: Template zulu-task-4 config
      ansible.builtin.template:
        src: templates/zulu-task-4.j2
        dest: /etc/charlie/zulu-task-4.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart charlie service
      ansible.builtin.service:
        name: charlie
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:43Z
